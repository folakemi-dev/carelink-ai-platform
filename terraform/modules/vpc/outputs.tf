output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "ID of the Jenkins public subnet"
  value       = aws_subnet.public.id
}

output "eks_public_subnet_ids" {
  description = "IDs of the EKS public subnets"
  value       = aws_subnet.eks_public[*].id
}
