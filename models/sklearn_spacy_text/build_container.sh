#!/bin/bash

docker build . -t sklearn_spacy_text_trainer
docker tag sklearn_spacy_text_trainer:latest gcr.io/ml-cicd/sklearn_spacy_text_trainer:latest
docker push gcr.io/ml-cicd/sklearn_spacy_text_trainer:latest

