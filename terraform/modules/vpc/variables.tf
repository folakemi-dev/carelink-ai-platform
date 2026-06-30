variable "project_name" {
  description = "Project name used for resource tagging"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "public_subnet_cidr" {
  description = "CIDR block for the Jenkins public subnet"
  type        = string
}

variable "eks_public_subnet_cidrs" {
  description = "CIDR blocks for EKS public subnets"
  type        = list(string)
}
