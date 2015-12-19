#!/bin/bash

# This is a script to build the modules and run the test suite in the base
# Docker container.

die() {
  echo "Error: $@" 1>&2
  exit 1;
}

cd /usr/src/ITKIOTransformDCMTK
source_sha=$(git rev-parse --short HEAD)
current_branch=$(git rev-parse --abbrev-ref HEAD)
topic=${TOPIC:=${current_branch}}
buildname="External-ITKIOTransformDCMTK-${topic}-${source_sha}"

cd /usr/src/ITKIOTransformDCMTK-build || die "Could not cd into the build directory"

cmake \
  -G Ninja \
  -DITK_DIR:PATH=/usr/src/ITK-build \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  "-DBUILDNAME=${buildname}" \
    /usr/src/ITKIOTransformDCMTK || die "CMake configuration failed"
ctest -VV -D Experimental || die "ctest failed"
