# Copyright 2019 Google LLC. This software is provided as-is, without warranty
# or representation for any use or purpose. Your use of it is subject to your
# agreement with Google.

FROM debian

ENV KSONNET_DOWNLOAD_URL https://github.com/ksonnet/ksonnet/releases/download/v0.13.1/ks_0.13.1_linux_amd64.tar.gz
ENV KUBECTL_DOWNLOAD_URL https://storage.googleapis.com/kubernetes-release/release/v1.11.2/bin/linux/amd64/kubectl
ENV KUBERNETES_DOWNLOAD_URL https://github.com/kubernetes/kubernetes/archive/v1.11.2.tar.gz
ENV KUBEFLOW_URL https://github.com/kubeflow/kubeflow
ENV KUBEFLOW_VERSION v0.4.1

RUN apt-get update -q && apt-get upgrade -y && \
    apt-get install -y -qq --no-install-recommends \
      apt-transport-https \
      ca-certificates \
      curl \
      git \
      gnupg \
      lsb-release \
      software-properties-common \
      unzip \
      wget && \
    wget -O /opt/ks_0.13.1_linux_amd64.tar.gz \
      $KSONNET_DOWNLOAD_URL && \
    tar -C /opt -xzf /opt/ks_0.13.1_linux_amd64.tar.gz && \
    cp /opt/ks_0.13.1_linux_amd64/ks /bin/. && \
    rm -f /opt/ks_0.13.1_linux_amd64.tar.gz && \
    wget -O /bin/kubectl \
      $KUBECTL_DOWNLOAD_URL && \
    chmod u+x /bin/kubectl && \
    wget -O /opt/kubernetes_v1.11.2 \
      $KUBERNETES_DOWNLOAD_URL && \
    mkdir -p /src && \
    tar -C /src -xzf /opt/kubernetes_v1.11.2 && \
    rm -rf /opt/kubernetes_v1.11.2

ADD ./src /serving_deployer

WORKDIR /

ENTRYPOINT ["/serving_deployer/deploy_seldon.sh"]

