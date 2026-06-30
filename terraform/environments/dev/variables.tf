variable "aws_region" {
  description = "AWS region for the development environment"
  type        = string
}

variable "project_name" {
  description = "Project name used for tagging AWS resources"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for the development VPC"
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

variable "key_name" {
  description = "Existing AWS EC2 key pair name for SSH access"
  type        = string
}

variable "allowed_ssh_cidr" {
  description = "Your public IP address in CIDR format for SSH access"
  type        = string
}

variable "allowed_jenkins_cidr" {
  description = "Your public IP address in CIDR format for Jenkins web access"
  type        = string
}

variable "eks_node_instance_types" {
  description = "EC2 instance types for EKS worker nodes"
  type        = list(string)
}

variable "eks_node_desired_size" {
  description = "Desired number of EKS worker nodes"
  type        = number
}

variable "eks_node_min_size" {
  description = "Minimum number of EKS worker nodes"
  type        = number
}

variable "eks_node_max_size" {
  description = "Maximum number of EKS worker nodes"
  type        = number
}
