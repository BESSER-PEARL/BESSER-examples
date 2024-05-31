provider "aws" {
    region = "us-east-1"
    access_key = "" # Enter AWS IAM

    secret_key = "" # Enter AWS IAM

  }
  
  terraform {
    required_providers {
      aws = {
        source  = "hashicorp/aws"
        version = "~> 3.0"
      }
    }
  }
  