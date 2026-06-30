output "jenkins_role_name" {
  description = "Name of the Jenkins IAM role"
  value       = aws_iam_role.jenkins.name
}

output "jenkins_instance_profile_name" {
  description = "Name of the Jenkins IAM instance profile"
  value       = aws_iam_instance_profile.jenkins.name
}
