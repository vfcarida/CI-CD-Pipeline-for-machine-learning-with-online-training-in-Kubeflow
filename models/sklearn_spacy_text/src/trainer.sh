#!/bin/bash

# Authenticate using the service account file set by Kubeflow. This is necessary
# to bypass VM scope restrictions
gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS

TRAIN_DATA_GCS_PATH=$1
EVAL_DATA_GCS_PATH=$2
OUTPUT_GCS_PATH=$3

TRAIN_DATA_LOCAL_PATH=/tmp/train_data.csv
EVAL_DATA_LOCAL_PATH=/tmp/eval_data.csv
OUTPUT_LOCAL_FILE=/tmp/model.pkl
CODE_TARBALL=/tmp/model.tar.gz

mkdir -p $(dirname $TRAIN_DATA_LOCAL_PATH)
mkdir -p $(dirname $EVAL_DATA_LOCAL_PATH)

gsutil cp $TRAIN_DATA_GCS_PATH $TRAIN_DATA_LOCAL_PATH
gsutil cp $EVAL_DATA_GCS_PATH $EVAL_DATA_LOCAL_PATH

python3 /sklearn_spacy_text/trainer.py \
  $TRAIN_DATA_LOCAL_PATH \
  $EVAL_DATA_LOCAL_PATH \
  $OUTPUT_LOCAL_FILE

TRAIN_ERR=$?

if [ $TRAIN_ERR -eq 0 ]
then
  # Package and upload code
  cd /sklearn_spacy_text
  tar czvf $CODE_TARBALL *
  gsutil cp $CODE_TARBALL $OUTPUT_GCS_PATH/

  # Upload PKL file
  gsutil cp $OUTPUT_LOCAL_FILE $OUTPUT_GCS_PATH/
  echo "$OUTPUT_GCS_PATH" >/output.txt
else
  exit $TRAIN_ERR
fi
