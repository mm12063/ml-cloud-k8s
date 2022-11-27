#!/bin/bash

# Login to IBM Cloud
make iclogin

# Download and update the ibm cloud cluster config file
ibmcloud ks cluster config --cluster mm12063-hw5-kube-cluster
