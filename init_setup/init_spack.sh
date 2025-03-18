#! /bin/bash

show_pw(){
  echo "headless"
}


show_pw | sudo -S apt update
shwo_pw | sudo -S apt install -y bzip2 ca-certificates g++ gcc gfortran git gzip lsb-release patch python3 tar unzip xz-utils zstd
