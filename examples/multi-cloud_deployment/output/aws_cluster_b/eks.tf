resource "aws_iam_role" "cluster_b" {
    name = "eks-cluster-cluster_b"
  
    assume_role_policy = <<POLICY
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "eks.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }
  POLICY
}
  
  resource "aws_iam_role_policy_attachment" "cluster_b-AmazonEKSClusterPolicy" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
    role       = aws_iam_role.cluster_b.name
  }
  
  variable "cluster_name" {
    default = "cluster_b"
    type = string
    description = "AWS EKS CLuster Name"
    nullable = false
  }
  
  resource "aws_eks_cluster" "cluster_b" {
    name     = var.cluster_name
    role_arn = aws_iam_role.cluster_b.arn
  
    vpc_config {
      subnet_ids = [
        aws_subnet.private-us-east-1a.id,
        aws_subnet.private-us-east-1b.id,
        aws_subnet.public-us-east-1a.id,
        aws_subnet.public-us-east-1b.id
      ]
    }
  
    depends_on = [aws_iam_role_policy_attachment.cluster_b-AmazonEKSClusterPolicy]
  }
  
  data "aws_eks_cluster_auth" "cluster" {
    name = aws_eks_cluster.cluster_b.id
  }
  provider "kubernetes" {
    host                   = aws_eks_cluster.cluster_b.endpoint
    cluster_ca_certificate = base64decode(aws_eks_cluster.cluster_b.certificate_authority.0.data)
    token                  = data.aws_eks_cluster_auth.cluster.token
  }
  
resource "kubernetes_deployment_v1" "default-" {
  wait_for_rollout = true
    metadata {
       name = "dpp_deployment" 
      labels = {
        app = "dpp_app"
      }
    }
    timeouts {
      create = "25m"
      update = "20m"
      delete = "20m"
    }
    spec {
  
      replicas = 2
      selector {
        match_labels = {
          app = "dpp_app"
        }
      }
      template {
        metadata {
          labels = {
            app = "dpp_app"
          }
        }
        spec {
          container {
            image = "dpp/app:latest"
            name  = "dpp_container"
            resources {
              limits = {
                cpu    = "500"
                memory = "512Mi"
              }
              requests = {
                cpu    = "10m"
                memory = "100Mi"
              }
            }
          }
        }
      }
    }
    depends_on = ["aws_eks_node_group.private-nodes"]
  }

resource "kubernetes_service_v1" "default-1" {
  metadata {
    name = "dpp_service"
#    namespace = kubernetes_namespace.app_namespace.metadata[0].name
  }
  spec {
    selector = {
      app = "dpp_app"
    }
    port {
      protocol    = "TCP"
      port        = 80
      target_port = 8000
    }
    type = "LoadBalancer"
  }
}

