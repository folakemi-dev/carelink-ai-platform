variable "project_name" {
  description = "Project name used for resource tagging"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID where the security group will be created"
  type        = string
}

variable "allowed_ssh_cidr" {
  description = "CIDR allowed to access SSH"
  type        = string
}

variable "allowed_jenkins_cidr" {
  description = "CIDR allowed to access Jenkins"
  type        = string
}
