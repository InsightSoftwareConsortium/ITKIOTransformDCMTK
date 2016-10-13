FROM debian:8
MAINTAINER Insight Software Consortium <community@itk.org>

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  cmake \
  git \
  libexpat1-dev \
  libhdf5-dev \
  libjpeg-dev \
  libpng12-dev \
  libpython3-dev \
  libtiff5-dev \
  python \
  ninja-build \
  wget \
  vim \
  zlib1g-dev

WORKDIR /usr/src
RUN git clone https://github.com/Kitware/KWStyle.git && \
  mkdir -p KWStyle-build && \
  cd KWStyle-build && \
  cmake \
    -DCMAKE_BUILD_TYPE:STRING=Release \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -G Ninja \
    ../KWStyle && \
  ninja && \
  ctest && \
  ninja install && \
  cd .. && rm -rf KWStyle*

# 2016-10-12
ENV ITK_GIT_TAG 6327e3b441cfb84baafae8133443a8c455c557db
RUN git clone git://itk.org/ITK.git && \
  cd ITK && \
  git checkout ${ITK_GIT_TAG} && \
  cd ../ && \
  mkdir ITK-build && \
  cd ITK-build && \
  cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=/usr \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DBUILD_TESTING:BOOL=OFF \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DITK_LEGACY_REMOVE:BOOL=ON \
    -DITK_BUILD_DEFAULT_MODULES:BOOL=OFF \
    -DITK_USE_SYSTEM_LIBRARIES:BOOL=ON \
    -DModule_ITKIOTransformBase:BOOL=ON \
    -DModule_ITKDCMTK:BOOL=ON \
    -DModule_ITKIODCMTK:BOOL=ON \
    -DModule_ITKIOGDCM:BOOL=ON \
    -DModule_ITKImageGrid:BOOL=ON \
    -DModule_ITKTestKernel:BOOL=ON \
    ../ITK && \
  make -j$(nproc) && \
  find . -name '*.o' -delete

RUN mkdir -p /usr/src/ITKIOTransformDCMTK-build
