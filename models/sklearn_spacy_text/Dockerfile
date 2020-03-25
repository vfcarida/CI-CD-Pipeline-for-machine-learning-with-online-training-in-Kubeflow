# Copyright 2019 Google LLC. This software is provided as-is, without warranty
# or representation for any use or purpose. Your use of it is subject to your
# agreement with Google.

FROM ubuntu:18.10

RUN apt-get update -y && apt-get install --no-install-recommends -y -q \
    ca-certificates python3 python3-pip python3-dev python3-setuptools \
    python-numpy python-scipy build-essential autoconf libtool pkg-config

# Install gcloud to copy files from/to GCS
RUN apt-get update -q && apt-get upgrade -y && \
    apt-get install -y -qq --no-install-recommends \
      apt-transport-https \
      git \
      gnupg \
      lsb-release \
      unzip \
      wget && \
    wget -O /opt/google-apt-key.gpg \
      https://packages.cloud.google.com/apt/doc/apt-key.gpg && \
    apt-key add /opt/google-apt-key.gpg && \
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" >> \
      /etc/apt/sources.list.d/google-cloud-sdk.list && \
    apt-get update -q && \
    apt-get install -y -qq --no-install-recommends google-cloud-sdk && \
    gcloud config set component_manager/disable_update_check true

ADD ./src /sklearn_spacy_text

RUN pip3 install wheel
RUN pip3 install -r /sklearn_spacy_text/requirements.txt

WORKDIR /sklearn_spacy_text

ENTRYPOINT ["/sklearn_spacy_text/trainer.sh"]

