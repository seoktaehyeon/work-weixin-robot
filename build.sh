#!/bin/bash
set -ex
rm -rf build dist *.egg-info
python setup.py sdist bdist_wheel
twine upload dist/*
