# Working with K8S on IBM Cloud

This is a Vagrant created VM containing packages to work with IBM Cloud. 

First, please login to IBM Cloud and download the cluster config. Please ensure you have created a cluster using the name in /start_ic.sh. To login, execute:

sh start_ic.sh

To deploy the manifests, please execute the following:

## Deploy the required yaml files to K8S
kubectl apply -f training/deploy/pvc.yaml
kubectl apply -f training/deploy/pod.yaml
kubectl apply -f inference/deploy/deployment.yaml
kubectl apply -f inference/deploy/service.yaml

## Show the status of the cluster
kubectl get all
