output "repository_urls" {
  description = "Map of ECR repository URLs"
  value = {
    for name, repo in aws_ecr_repository.repositories :
    name => repo.repository_url
  }
}
