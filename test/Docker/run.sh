#!/bin/sh

script_dir="`cd $(dirname $0); pwd`"

docker run \
  --rm \
  -v $script_dir/../..:/usr/src/ITKIOTransformDCMTK \
    insighttoolkit/iotransformdcmtk-test \
      /usr/src/ITKIOTransformDCMTK/test/Docker/test.sh
