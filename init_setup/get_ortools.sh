#! /bin/bash

mkdir -p opt/or-tools
if [[ ! -f or-tools_amd64_ubuntu-22.04_cpp_v9.11.4210.tar.gz ]]; then
  wget https://github.com/google/or-tools/releases/download/v9.11/or-tools_amd64_ubuntu-22.04_cpp_v9.11.4210.tar.gz
fi
tar --strip 1 --dir opt/or-tools -xf or-tools_amd64_ubuntu-22.04_cpp_v9.11.4210.tar.gz

