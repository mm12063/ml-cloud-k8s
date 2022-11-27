#!/bin/bash

# Deploy the required yaml files to K8S
kubectl apply -f training/deploy/pvc.yaml
kubectl apply -f training/deploy/pod.yaml
kubectl apply -f inference/deploy/deployment.yaml
kubectl apply -f inference/deploy/service.yaml

# Show the status of the cluster
kubectl get all
