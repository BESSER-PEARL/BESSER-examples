resource "aws_iam_role" "demo" {
    name = "eks-cluster-demo"
  
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
  
  resource "aws_iam_role_policy_attachment" "demo-AmazonEKSClusterPolicy" {
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
    role       = aws_iam_role.demo.name
  }
  
  variable "cluster_name" {
    default = "demo"
    type = string
    description = "AWS EKS CLuster Name"
    nullable = false
  }
  
  resource "aws_eks_cluster" "demo" {
    name     = var.cluster_name
    role_arn = aws_iam_role.demo.arn
  
    vpc_config {
      subnet_ids = [
        aws_subnet.private-us-east-1a.id,
        aws_subnet.private-us-east-1b.id,
        aws_subnet.public-us-east-1a.id,
        aws_subnet.public-us-east-1b.id
      ]
    }
  
    depends_on = [aws_iam_role_policy_attachment.demo-AmazonEKSClusterPolicy]
  }
  
  data "aws_eks_cluster_auth" "cluster" {
    name = aws_eks_cluster.demo.id
  }
  provider "kubernetes" {
    host                   = aws_eks_cluster.demo.endpoint
    cluster_ca_certificate = base64decode(aws_eks_cluster.demo.certificate_authority.0.data)
    token                  = data.aws_eks_cluster_auth.cluster.token
  }
  
resource "kubernetes_deployment_v1" "default-" {
  wait_for_rollout = true
    metadata {
       name = "deployment1" 
      labels = {
        app = "app1"
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
          app = "app1"
        }
      }
      template {
        metadata {
          labels = {
            app = "app1"
          }
        }
        spec {
          container {
            image = "image/latest"
            name  = "container1"
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
    name = "service1"
#    namespace = kubernetes_namespace.app_namespace.metadata[0].name
  }
  spec {
    selector = {
      app = "app1"
    }
    port {
      protocol    = "TCP"
      port        = 80
      target_port = 8000
    }
    type = "LoadBalancer"
  }
}

resource "kubernetes_ingress_v1" "example" {
  wait_for_load_balancer = true
  metadata {
    name = "example"
  }
  spec {
    rule {
      http {
        path {
          path = "/*"
          backend {
            service {
              name = kubernetes_service_v1.default-1.metadata.0.name
              port {
                number = 80
              }
            }
          }
        }
      }
    }
  }
}
