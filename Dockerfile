ARG IMAGE=intersystemsdc/iris-community:latest
FROM $IMAGE

USER root   
        
WORKDIR /irisdev/app
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /irisdev/app
USER ${ISC_PACKAGE_MGRUSER}

COPY Installer.cls .
COPY src src
COPY iris.script /tmp/iris.script

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN iris start IRIS \
	&& iris session IRIS < /tmp/iris.script \
    && iris stop IRIS quietly

ENV IRISUSERNAME "SuperUser"
ENV IRISPASSWORD "SYS"
ENV IRISNAMESPACE "IRISAPP"

