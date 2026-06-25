pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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
                sh 'docker build -t carelink-frontend:jenkins services/frontend'
                sh 'docker build -t carelink-api-gateway:jenkins services/api-gateway'
                sh 'docker build -t carelink-auth-service:jenkins services/auth-service'
                sh 'docker build -t carelink-patient-service:jenkins services/patient-service'
                sh 'docker build -t carelink-appointment-service:jenkins services/appointment-service'
                sh 'docker build -t carelink-notification-service:jenkins services/notification-service'
                sh 'docker build -t carelink-ai-service:jenkins services/ai-service'
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
            echo 'CareLink Jenkins pipeline completed successfully.'
        }

        failure {
            echo 'CareLink Jenkins pipeline failed. Check the failed stage logs.'
        }
    }
}
