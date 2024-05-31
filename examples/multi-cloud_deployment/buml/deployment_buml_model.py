from besser.BUML.metamodel.deployment import *

# Deployment architecture model definition

dpp_app : Application = Application(name="dpp_app", image_repo="dpp/app:latest", port=8000, required_resources=Resources(cpu=10, memory=100), domain_model="library_model")
dpp_service : Service = Service(name="dpp_service", port=80, target_port=8000, protocol=Protocol.tcp, type=ServiceType.lb, application=dpp_app)
dpp_container : Container = Container(name="dpp_container", application=dpp_app, resources_limit=Resources(cpu=500, memory=512))
dpp_deployment : Deployment = Deployment(name="dpp_deployment", replicas=2, containers={dpp_container})
us_east : Region = Region(name="us-east", zones={})

# Public cluster definition
cluster_a : PublicCluster = PublicCluster(name="cluster_a", num_nodes=3, provider=Provider.google, config_file="config_google.conf", services={dpp_service}, deployments={dpp_deployment}, regions={us_east})

# Public cluster definition
cluster_b : PublicCluster = PublicCluster(name="cluster_b", num_nodes=3, provider=Provider.aws, config_file="config_aws.conf", services={dpp_service}, deployments={dpp_deployment}, regions={us_east})

# Deployment architecture model definition
deployment_model : DeploymentModel = DeploymentModel(name="deployment_model", clusters={cluster_a, cluster_b})
