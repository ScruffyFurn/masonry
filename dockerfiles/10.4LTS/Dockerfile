FROM archlinux/archlinux:base-devel

RUN pacman -Syu --needed --noconfirm git

# mason user and workdir
ARG user=mason
RUN useradd --system --create-home $user \
  && echo "$user ALL=(ALL:ALL) NOPASSWD:ALL" > /etc/sudoers.d/$user
USER $user
WORKDIR /home/$user

# Install yay
RUN git clone https://aur.archlinux.org/yay.git \
  && cd yay \
  && makepkg -sri --needed --noconfirm \
  && cd \
  # Clean up
  && rm -rf .cache yay

# Install python 3.8
RUN yay -Syu --needed --noconfirm python38
RUN sudo ln -s /usr/bin/python3.8 /usr/bin/python3
RUN sudo ln -s /usr/bin/python3.8 /usr/bin/python

# Install java
RUN yay -Syu --needed --noconfirm jdk8-openjdk

# Install pip
RUN sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN sudo python3.8 get-pip.py

# Install Azure CLI
RUN yay -Syu --needed --noconfirm azure-cli

# Install Databricks-connect, Databricks-cli
WORKDIR /
COPY requirements.txt .
RUN sudo pip install -r requirements.txt
RUN sudo rm requirements.txt
COPY create_new_library.sh /usr/local/bin/masonry
RUN sudo chmod +x /usr/local/bin/masonry