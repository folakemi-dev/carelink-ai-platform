pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-2'
        PROJECT_NAME = 'carelink-ai'
        SERVICES = 'frontend api-gateway auth-service patient-service appointment-service notification-service ai-service'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Build Variables') {
            steps {
                script {
                    env.IMAGE_TAG = sh(
                        script: 'git rev-parse --short HEAD',
                        returnStdout: true
                    ).trim()

                    env.AWS_ACCOUNT_ID = sh(
                        script: 'aws sts get-caller-identity --query Account --output text',
                        returnStdout: true
                    ).trim()

                    env.ECR_REGISTRY = "${env.AWS_ACCOUNT_ID}.dkr.ecr.${env.AWS_REGION}.amazonaws.com"
                }

                echo "Image tag: ${IMAGE_TAG}"
                echo "ECR registry: ${ECR_REGISTRY}"
            }
        }

        stage('Build Frontend') {
            steps {
                dir('services/frontend') {
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                    for SERVICE in $SERVICES; do
                      echo "Building Docker image for $SERVICE"
                      docker build -t carelink-$SERVICE:$IMAGE_TAG ./services/$SERVICE
                    done
                '''
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh '''
                    for SERVICE in $SERVICES; do
                      echo "Scanning carelink-$SERVICE:$IMAGE_TAG with Trivy"
                      trivy image --no-progress --severity HIGH,CRITICAL --exit-code 0 carelink-$SERVICE:$IMAGE_TAG
                    done
                '''
            }
        }

        stage('Login to Amazon ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REGISTRY
                '''
            }
        }

        stage('Tag and Push Images to ECR') {
            steps {
                sh '''
                    for SERVICE in $SERVICES; do
                      LOCAL_IMAGE="carelink-$SERVICE:$IMAGE_TAG"
                      ECR_IMAGE="$ECR_REGISTRY/$PROJECT_NAME/$SERVICE:$IMAGE_TAG"
                      ECR_LATEST="$ECR_REGISTRY/$PROJECT_NAME/$SERVICE:latest"

                      echo "Tagging $LOCAL_IMAGE as $ECR_IMAGE"
                      docker tag $LOCAL_IMAGE $ECR_IMAGE
                      docker tag $LOCAL_IMAGE $ECR_LATEST

                      echo "Pushing $ECR_IMAGE"
                      docker push $ECR_IMAGE

                      echo "Pushing $ECR_LATEST"
                      docker push $ECR_LATEST
                    done
                '''
            }
        }

        stage('Validate Helm Chart') {
            steps {
                sh 'helm lint helm/carelink'
                sh 'helm template carelink-jenkins helm/carelink'
            }
        }
    }

    post {
        success {
            echo 'CareLink Jenkins pipeline completed successfully. Images were scanned and pushed to ECR.'
        }

        failure {
            echo 'CareLink Jenkins pipeline failed. Check the failed stage logs.'
        }
    }
}
