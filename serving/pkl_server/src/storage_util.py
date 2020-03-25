#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2019 Google LLC. This software is provided as-is, without warranty
# or representation for any use or purpose. Your use of it is subject to your
# agreement with Google.

import os
import re
from google.cloud import storage


def download_blob(source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket_name, blob_path = get_bucket_from_uri(source_blob_name)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_path)

    blob.download_to_filename(destination_file_name)

    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))


def copy_file_to_object_storage(local_file_path, object_store_path):
  print("Copy file {0} to {1}".format(local_file_path, object_store_path))
  bucket_name, blob_path = get_bucket_from_uri(object_store_path)

  _, file_name = os.path.split(local_file_path)
  blob_path = os.path.join(blob_path, file_name)

  storage_client = storage.Client()
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(blob_path)
  output_path = os.path.join('gs://' + bucket_name, blob_path)

  blob.upload_from_filename(local_file_path)

  print("Copying file {0} to bucket {1}, blob {2}".format(local_file_path, bucket_name, blob_path))

  return output_path


def get_bucket_from_uri(uri):

  regex = r"gs:\/\/([^\/]*)\/(.*)"

  match = re.search(regex, uri)

  bucket_name = None
  blob_path = None
  if match:
    bucket_name = match.group(1)
    blob_path = match.group(2)

  return bucket_name, blob_path

