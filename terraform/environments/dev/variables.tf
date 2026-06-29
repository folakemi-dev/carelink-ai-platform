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
  description = "CIDR block for the public subnet"
  type        = string
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
