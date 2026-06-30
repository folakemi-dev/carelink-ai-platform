module "vpc" {
  source = "../../modules/vpc"

  project_name            = var.project_name
  environment             = var.environment
  vpc_cidr                = var.vpc_cidr
  public_subnet_cidr      = var.public_subnet_cidr
  eks_public_subnet_cidrs = var.eks_public_subnet_cidrs
}

module "security_groups" {
  source = "../../modules/security-groups"

  project_name         = var.project_name
  environment          = var.environment
  vpc_id               = module.vpc.vpc_id
  allowed_ssh_cidr     = var.allowed_ssh_cidr
  allowed_jenkins_cidr = var.allowed_jenkins_cidr
}

module "iam" {
  source = "../../modules/iam"

  project_name = var.project_name
  environment  = var.environment
}

module "jenkins" {
  source = "../../modules/jenkins"

  project_name         = var.project_name
  environment          = var.environment
  subnet_id            = module.vpc.public_subnet_id
  security_group_id    = module.security_groups.jenkins_security_group_id
  key_name             = var.key_name
  iam_instance_profile = module.iam.jenkins_instance_profile_name
}

module "ecr" {
  source = "../../modules/ecr"

  project_name = var.project_name
  environment  = var.environment

  repositories = [
    "frontend",
    "api-gateway",
    "auth-service",
    "patient-service",
    "appointment-service",
    "notification-service",
    "ai-service"
  ]
}

module "eks" {
  source = "../../modules/eks"

  project_name        = var.project_name
  environment         = var.environment
  subnet_ids          = module.vpc.eks_public_subnet_ids
  node_instance_types = var.eks_node_instance_types
  node_desired_size   = var.eks_node_desired_size
  node_min_size       = var.eks_node_min_size
  node_max_size       = var.eks_node_max_size
}
