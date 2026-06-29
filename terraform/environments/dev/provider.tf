terraform {
  required_version = ">= 1.5.0"

  backend "s3" {
    bucket         = "carelink-ai-terraform-state-593696434222-us-east-2"
    key            = "environments/dev/terraform.tfstate"
    region         = "us-east-2"
    dynamodb_table = "carelink-ai-terraform-locks"
    encrypt        = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}