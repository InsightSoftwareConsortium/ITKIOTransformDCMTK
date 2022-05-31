# -*- coding: utf-8 -*-
from __future__ import print_function
from os import sys

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

setup(
    name='itk-iotransformdcmtk',
    version='1.0.0',
    author='Matthew M. McCormick',
    author_email='matt.mccorcmick@kitware.com',
    packages=['itk'],
    package_dir={'itk': 'itk'},
    download_url=r'https://github.com/InsightSoftwareConsortium/ITKIOTransformDCMTK',
    description=r'ITK classes to read DICOM spatial transforms',
    long_description='itk-iotransformdcmtk provides classes to read DICOM '
                     'Spatial Registration Object files into `itk::Transform`\'s.\n'
                     'Please refer to:\n'
                     'M. McCormick, K. Wang, A. Lasso, G. Sharp, S. Pieper, '
                     '"DICOM Spatial Transform IO in the Insight Toolkit.", '
                     'Insight Journal, January-December 2014, https://hdl.handle.net/10380/3468.',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: C++",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
    license='Apache',
    keywords='ITK InsightToolkit DICOM Registration',
    url=r'https://github.com/InsightSoftwareConsortium/ITKIOTransformDCMTK',
    install_requires=[
        r'itk'
    ]
    )
