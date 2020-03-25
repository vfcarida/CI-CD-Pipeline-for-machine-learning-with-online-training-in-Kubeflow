#!/bin/bash

MODEL_NAME=$1
MODEL_GCS_PATH=$2
MODEL_VERSION=$3

echo MODEL_NAME=$MODEL_NAME
echo MODEL_GCS_PATH=$MODEL_GCS_PATH
echo MODEL_VERSION=$MODEL_VERSION

DEPLOYMENT_NAME=$MODEL_NAME-$MODEL_VERSION
SPEC_NAME=$MODEL_NAME-spec-$MODEL_VERSION
PREDICTOR_NAME=$MODEL_NAME-predictor-$MODEL_VERSION

IMAGE=pkl_server
VERSION=latest
REPO=gcr.io/ml-cicd

SELDON_CONFIG_FILE=./seldon_config.yaml

cat >$SELDON_CONFIG_FILE <<EOF
apiVersion: machinelearning.seldon.io/v1alpha2
kind: SeldonDeployment
metadata:
  name: $DEPLOYMENT_NAME
spec:
  name: $SPEC_NAME
  predictors:
  - componentSpecs:
    - spec:
        containers:
        - image: ${REPO}/${IMAGE}:${VERSION}
          name: classifier
    graph:
      children: []
      endpoint:
        type: REST
      name: classifier
      type: MODEL
      parameters:
      - type: STRING
        name: pkl_path
        value: $MODEL_GCS_PATH
    name: $PREDICTOR_NAME
    replicas: 1
EOF

echo "Deploying configuration file $SELDON_CONFIG_FILE"
cat $SELDON_CONFIG_FILE

kubectl apply -n kubeflow -f $SELDON_CONFIG_FILE

DEPLOY_ERR=$?

if [ $DEPLOY_ERR -eq 0 ]
then
  echo "http://localhost:8080/seldon/$DEPLOYMENT_NAME/api/v0.1/predictions" >/output.txt
else
  exit $DEPLOY_ERR
fi
