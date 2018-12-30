#!/bin/sh

mkdir venv
virtualenv -p python3 venv

pip install -r requirements.txt

# setup jupyter theme to dark
jt -t onedork

jupyter contrib nbextension install