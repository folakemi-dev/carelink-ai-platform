variable "project_name" {
  description = "Project name used for resource tagging"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "subnet_id" {
  description = "Public subnet ID where the Jenkins server will run"
  type        = string
}

variable "security_group_id" {
  description = "Security group ID attached to the Jenkins server"
  type        = string
}

variable "key_name" {
  description = "Existing AWS EC2 key pair name for SSH access"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type for the Jenkins server"
  type        = string
  default     = "t3.small"
}

variable "root_volume_size" {
  description = "Root EBS volume size in GiB"
  type        = number
  default     = 20
}
