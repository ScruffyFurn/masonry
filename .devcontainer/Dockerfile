FROM  --platform=linux/amd64 masonrydb/masonry:11.3LTS-Lite

WORKDIR /
COPY requirements.txt .
RUN sudo pip install -r requirements.txt
RUN sudo rm requirements.txt