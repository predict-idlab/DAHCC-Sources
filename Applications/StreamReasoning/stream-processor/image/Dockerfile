FROM openjdk:8
LABEL maintainer="Mathias De Brouwer, mrdbrouw.DeBrouwer@UGent.be"

# update all packages and install necessary tools
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y apt-utils software-properties-common curl ca-certificates wget gettext-base && \
    apt-get clean -y

# set application directory
ENV HOME_DIR /root/rsps
WORKDIR ${HOME_DIR}

# install Python and Python requirements
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

# copy all files
COPY . .

# run RSP engine starting script when creating container
ENTRYPOINT ["bash", "start-rsp-engine.sh"]
