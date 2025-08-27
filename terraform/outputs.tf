output "sonarqube_public_ip" {
  description = "Public IP of the SonarQube EC2 instance"
  value       = aws_instance.sonarqube.public_ip
}

output "security_group_id" {
  description = "Security Group ID used by the SonarQube instance"
  value       = aws_security_group.sonar_sg.id
}

output "subnet_id" {
  description = "Subnet ID where SonarQube instance is deployed"
  value       = aws_instance.sonarqube.subnet_id
}

output "instance_id" {
  description = "Instance ID of the SonarQube EC2"
  value       = aws_instance.sonarqube.id
}
