resource "aws_ecr_repository" "repositories" {
  for_each = toset(var.repositories)

  name                 = "${var.project_name}/${each.value}"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name        = "${var.project_name}-${each.value}"
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}
