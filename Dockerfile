FROM python:3.8-rc-stretch

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
    && pip install preview-generator

WORKDIR /var/app