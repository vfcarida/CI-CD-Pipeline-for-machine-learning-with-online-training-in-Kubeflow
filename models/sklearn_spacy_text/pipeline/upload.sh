#!/bin/bash

FILE_NAME=$1
PIPELINE_NAME=$2

curl -F "uploadfile=@$FILE_NAME" http://localhost:8080/pipeline/apis/v1beta1/pipelines/upload?name=$PIPELINE_NAME

