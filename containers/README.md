# Containers in GCP

- Google Container Registry

## Kubernetes Engine

- __Kubernetes__: 

Open source orchestrator for containers.
- Application config
- Managing updates
- Monitoring
- Scaling
- Resiliency

Deploy containers on a set of nodes called `cluster`.
- Master Node: controls the system as whole
- Nodes: Computing instance
- How applications interact with each other?

Kubernetes has an API that lets people to control his operation:
- kubectl

__How to get a Kubernetes cluster?__

Can use Kubernetes Engine (kubernetes as a managed service in the cloud)

```bash
gcloud container clusters create k1
```

GKE clusters can be customized and support:
- Machine Types
- Number of Nodes
- Network Settings

Whenever Kubernetes deploys a container or a set of related containers it do so inside a `pod`. A `pod` is the smallest deployable unit on kubernetes. Think as one process in the cluster (could be 1 component of your application or even the entire application). 
- It's common to have 1 container per `pod`, but, if you have multiple containers with a hard dependency, they can be packaged into a single `pod`, automatically share networking and have disk storage volumes in common. 
- Each `pod` gets a unique IP address in the cluster and set of ports for the containers.
- 

kubectl starts a `deployment`. A `deployment` represents a group of replicas of the same `pod`, keeps pods running even if a node where some of them fails. 

By default `pods` in the `deployment` are only accessible inside your cluster. To make `pods` in your `deployment` publicly available you can connect a `load balancer` to it. Kubernetes then create a `service` with a fixed IP address for the `pods`. A `service` is gthe fundamental way kubernetes represents load balancing. You request kubernetes to attach an external load balancer with a public IP address to the `service`. 

Kubernetes has a declarative way of definying full infrastructure, deployment strategy, autoscaling (using more replicas), way of grouping pods using labels to create a service and add an external load balancer.