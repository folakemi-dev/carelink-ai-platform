module "vpc" {
  source = "../../modules/vpc"

  project_name       = var.project_name
  environment        = var.environment
  vpc_cidr           = var.vpc_cidr
  public_subnet_cidr = var.public_subnet_cidr
}

module "security_groups" {
  source = "../../modules/security-groups"

  project_name         = var.project_name
  environment          = var.environment
  vpc_id               = module.vpc.vpc_id
  allowed_ssh_cidr     = var.allowed_ssh_cidr
  allowed_jenkins_cidr = var.allowed_jenkins_cidr
}

module "jenkins" {
  source = "../../modules/jenkins"

  project_name      = var.project_name
  environment       = var.environment
  subnet_id         = module.vpc.public_subnet_id
  security_group_id = module.security_groups.jenkins_security_group_id
  key_name          = var.key_name
}
