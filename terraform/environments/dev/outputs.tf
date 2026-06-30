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

output "jenkins_public_ip" {
  description = "Public IP address of the Jenkins server"
  value       = module.jenkins.jenkins_public_ip
}

output "jenkins_url" {
  description = "Jenkins web URL"
  value       = module.jenkins.jenkins_url
}

output "ecr_repository_urls" {
  description = "ECR repository URLs for CareLink services"
  value       = module.ecr.repository_urls
}

output "eks_public_subnet_ids" {
  description = "Public subnet IDs for EKS worker nodes"
  value       = module.vpc.eks_public_subnet_ids
}

output "eks_cluster_name" {
  description = "EKS cluster name"
  value       = module.eks.cluster_name
}

output "eks_cluster_endpoint" {
  description = "EKS cluster endpoint"
  value       = module.eks.cluster_endpoint
}

output "eks_node_group_name" {
  description = "EKS managed node group name"
  value       = module.eks.node_group_name
}
