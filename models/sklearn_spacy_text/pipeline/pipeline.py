#!/usr/bin/env python3

# Copyright 2019 Google LLC. This software is provided as-is, without warranty
# or representation for any use or purpose. Your use of it is subject to your
# agreement with Google.

import kfp
from kfp import components
from kfp import dsl
from kfp import gcp

# confusion_matrix_op = components.load_component_from_url(
#     'https://raw.githubusercontent.com/kubeflow/pipelines/eb830cd73ca148e5a1a6485a9374c2dc068314bc/components/local/confusion_matrix/component.yaml'
# )
# roc_op = components.load_component_from_url(
#     'https://raw.githubusercontent.com/kubeflow/pipelines/eb830cd73ca148e5a1a6485a9374c2dc068314bc/components/local/roc/component.yaml'
# )


def train_op(train_data, eval_data, output):
  return dsl.ContainerOp(
      name='train_sklearn_spacy_text_model',
      image='gcr.io/ml-cicd/sklearn_spacy_text_trainer:latest',
      arguments=[
          train_data,
          eval_data,
          output,
      ],
      file_outputs={
          'model_path': '/output.txt',
      })


def deploy_op(model_name, model_path, model_version):
  return dsl.ContainerOp(
      name='deploy_sklearn_spacy_text',
      image='gcr.io/ml-cicd/serving_deployer:latest',
      arguments=[
          model_name,
          model_path,
          model_version,
      ],
      file_outputs={
          'output': '/output.txt',
      })


# =======================================================================


@dsl.pipeline(
    name='SKLearn Model Pipeline',
    description='A pipeline that does end-to-end training and deployment for SKLearn models.')
def train_deploy_pipeline(
    model_path='gs://ml-cicd/models/sklearn_spacy_text',
    train_data='gs://ml-cicd/data/sklearn_spacy_text/train/train.csv',
    eval_data='gs://ml-cicd/data/sklearn_spacy_text/train/train.csv',
    model_version='000'
):
  model_name = 'sklearn-spacy-text'

  output_path = "{}/{}/{}".format(model_path, model_name, model_version)

  train_operation = train_op(train_data, eval_data, output_path).apply(
                          gcp.use_gcp_secret('user-gcp-sa'))

  deploy_operation = deploy_op(model_name,
                               train_operation.outputs["model_path"],
                               model_version)

  # predict_op = predict_op(
  #     project,
  #     region,
  #     create_cluster_op.output,
  #     transform_op.outputs['eval'],
  #     train_op.output,
  #     target,
  #     analyze_op.output,
  #     output_template
  # ).apply(gcp.use_gcp_secret('user-gcp-sa'))

  # confusion_matrix_task = confusion_matrix_op(
  #     predict_op.output,
  #     output_template
  # ).apply(gcp.use_gcp_secret('user-gcp-sa'))

  # roc_task = roc_op(
  #     predictions_dir=predict_op.output,
  #     true_class=true_label,
  #     true_score_column=true_label,
  #     output_dir=output_template
  # ).apply(gcp.use_gcp_secret('user-gcp-sa'))


if __name__ == '__main__':
  kfp.compiler.Compiler().compile(train_deploy_pipeline, __file__ + '.zip')
