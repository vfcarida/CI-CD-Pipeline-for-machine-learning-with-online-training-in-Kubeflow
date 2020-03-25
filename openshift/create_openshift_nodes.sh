#!/bin/sh

gcloud compute instances create openshift2-master --image=rhel-7-v20190423 --image-project=rhel-cloud --machine-type=n1-standard-8 --boot-disk-size=100GB --zone us-east1-b --scopes=https://www.googleapis.com/auth/cloud-platform
gcloud compute instances create openshift2-node1 --image=rhel-7-v20190423 --image-project=rhel-cloud --machine-type=n1-standard-4 --boot-disk-size=100GB --zone us-east1-b --scopes=https://www.googleapis.com/auth/cloud-platform
gcloud compute instances create openshift2-node2 --image=rhel-7-v20190423 --image-project=rhel-cloud --machine-type=n1-standard-4 --boot-disk-size=100GB --zone us-east1-b --scopes=https://www.googleapis.com/auth/cloud-platform
