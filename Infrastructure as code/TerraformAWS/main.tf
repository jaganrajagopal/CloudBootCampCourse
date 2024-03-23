provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow web inbound traffic"
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
  ami           = "ami-0c02fb55956c7d316" # Example AMI ID for Amazon Linux 2 in us-east-1
  instance_type = "t2.micro"
  security_groups = [aws_security_group.allow_web.name]
  associate_public_ip_address = true
  user_data = <<-EOF
              #!/bin/bash
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo '<h1>Welcome to Our  <a href="https://awstrainingwithjagan.com">Click Here AWSTrainingwithJagan </a>  Hosted on EC2</h1> 
              <p> You can check with github for more document <a href="https://github.com/jaganrajagopal/CloudBootCampCourse>Click Here </a>  ' > /var/www/html/index.html
              EOF

  tags = {
    Name = "WebServer"
  }
}
