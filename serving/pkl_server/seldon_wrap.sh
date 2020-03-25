#!/bin/sh

VERSION=latest
REPO=gcr.io/ml-cicd

IMAGE=pkl_server
SRC_DIR=src

# Build image with s2i (https://docs.seldon.io/projects/seldon-core/en/latest/python/python_wrapping.html)
s2i build $SRC_DIR seldonio/seldon-core-s2i-python36:0.7 ${IMAGE}
docker tag $IMAGE ${REPO}/${IMAGE}:${VERSION}

echo "Pushing image to ${REPO}/${IMAGE}:${VERSION}"
docker push ${REPO}/${IMAGE}:${VERSION}

# Deploy to the Kubeflow cluster
#kubectl apply -f $MODEL/avi_intencoes_seldon.yaml -n kubeflow

