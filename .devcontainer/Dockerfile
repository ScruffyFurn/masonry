FROM  --platform=linux/amd64 masonrydb/masonry:base

# Install Python requirements
WORKDIR /
COPY .devcontainer/requirements.txt .
RUN sudo pip install -r requirements.txt
