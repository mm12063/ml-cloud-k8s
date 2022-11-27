#!/bin/bash

ibmcloud plugin install container-service -r 'IBM Cloud'
ibmcloud plugin install container-registry -r 'IBM Cloud'
ibmcloud plugin install vpc-infrastructure -r 'IBM Cloud'
echo "Done!"

cd /vagrant/
make iclogin
ic ks cluster config --cluster mm12063-hw5-cluster-1-v2