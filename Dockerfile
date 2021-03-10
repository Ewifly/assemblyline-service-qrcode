FROM cccs/assemblyline-v4-service-base:latest

ENV SERVICE_PATH qrcode.QRCode

USER $USER
RUN apt-get update
RUN apt-get install -y libzbar0
RUN pip3 install xqrcode
RUN pip3 install pyzbar
# Install any service dependencies here
# For example: RUN apt-get update && apt-get install -y libyaml-dev
#              RUN pip install utils

# Switch to assemblyline user
USER assemblyline

# Copy QRCode service code
WORKDIR /opt/al_service
COPY . .
