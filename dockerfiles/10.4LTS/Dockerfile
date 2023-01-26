FROM masonrydb/masonry:base

# mason user and workdir
ARG user=mason
USER $user
WORKDIR /home/$user

# Install Databricks-connect, Databricks-cli
WORKDIR /
COPY requirements.txt .
RUN sudo pip install -r requirements.txt
RUN sudo rm requirements.txt
