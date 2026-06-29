output "vpc_id" {
  description = "Development VPC ID"
  value       = module.vpc.vpc_id
}

output "public_subnet_id" {
  description = "Development public subnet ID"
  value       = module.vpc.public_subnet_id
}

output "jenkins_security_group_id" {
  description = "Jenkins security group ID"
  value       = module.security_groups.jenkins_security_group_id
}

output "jenkins_instance_id" {
  description = "Jenkins EC2 instance ID"
  value       = module.jenkins.instance_id
}

output "jenkins_public_ip" {
  description = "Jenkins server public IP address"
  value       = module.jenkins.public_ip
}

output "jenkins_url" {
  description = "Jenkins web URL"
  value       = module.jenkins.jenkins_url
}
