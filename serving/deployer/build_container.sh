#!/bin/bash

docker build . -t serving_deployer
docker tag serving_deployer:latest gcr.io/ml-cicd/serving_deployer:latest
docker push gcr.io/ml-cicd/serving_deployer:latest

