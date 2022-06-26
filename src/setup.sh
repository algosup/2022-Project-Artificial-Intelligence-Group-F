#!/bin/bash

mkdir -p data/train/english data/train/french data/test/english data/test/french

mkdir -p datasets/english datasets/french

pip install -r requirements.txt

echo "Finished to create the folders"