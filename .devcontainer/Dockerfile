#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------
FROM scruffyfurn/masonry:base

# CMD
WORKDIR /
COPY .devcontainer/environment.yml .
RUN pip install --upgrade --no-cache-dir pip \
    && conda env create -f environment.yml \
    && echo '{}' > /root/.databricks-connect

