#!/bin/bash

# Install CMake
wget https://github.com/Kitware/CMake/releases/download/v3.26.4/cmake-3.26.4-linux-x86_64.sh
chmod +x cmake-3.26.4-linux-x86_64.sh
sudo ./cmake-3.26.4-linux-x86_64.sh --prefix=/usr/local --skip-license

# Ensure the installation was successful
cmake --version

# Install Python dependencies
pip install -r requirements.txt
