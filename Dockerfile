FROM python:3.7-rc-stretch
# using python 3.7 due to a regression
# in Python 3.8.0a3 and Werkzeug 0.15.4
# (https://github.com/pallets/werkzeug/issues/1551)

LABEL maintainer="andreschuelein@gmail.com"

COPY ./requirements.txt /var/app/requirements.txt

RUN apt-get update \
    &&  apt-get install -y \
    zlib1g-dev \
    libjpeg-dev \
    python3-pythonmagick \
    inkscape \
    xvfb \
    poppler-utils \
    libfile-mimeinfo-perl \
    qpdf \
    libreoffice \
    && wget https://sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-11.11.tar.gz \
    && gzip -dc Image-ExifTool-11.11.tar.gz | tar -xf - \
    && cd Image-ExifTool-11.11 \
    && perl Makefile.PL \
    && make install \
    && rm -f ../Image-ExifTool-11.11.tar.gz \
    && pip install --upgrade pip \
    && pip install -r /var/app/requirements.txt \
    && rm -f /var/app/requirements.txt

WORKDIR /var/app
COPY ./app/preview.py .
COPY entry_point.sh /
CMD /entry_point.sh