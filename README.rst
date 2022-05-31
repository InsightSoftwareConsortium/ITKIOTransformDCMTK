ITKIOTransformDCMTK
===================

.. |CircleCI| image:: https://circleci.com/gh/InsightSoftwareConsortium/ITKIOTransformDCMTK.svg?style=shield
    :target: https://circleci.com/gh/InsightSoftwareConsortium/ITKIOTransformDCMTK

.. |TravisCI| image:: https://travis-ci.org/InsightSoftwareConsortium/ITKIOTransformDCMTK.svg?branch=master
    :target: https://travis-ci.org/InsightSoftwareConsortium/ITKIOTransformDCMTK

.. |AppVeyor| image:: https://img.shields.io/appveyor/ci/itkrobot/itkiotransformdcmtk.svg
    :target: https://ci.appveyor.com/project/itkrobot/itkiotransformdcmtk

=========== =========== ===========
   Linux      macOS       Windows
=========== =========== ===========
|CircleCI|  |TravisCI|  |AppVeyor|
=========== =========== ===========


Overview
--------

An ITK module to read DICOM spatial transforms.

A module that extends the Insight Toolkit, `ITK <https://itk.org>`_, which
reads DICOM Spatial Registration Object files into `itk::Transform`'s. Currently,
DICOM files are read by applying the DCMTK library as a backend. An
`itk::DCMTKTransformIO` class can be registered with the IO factory mechanism
so `itk::TransformFileReaderTemplate` will recognize and read these files.

A more detailed description can be found in the `Insight Journal article <https://hdl.handle.net/10380/3468>`_::

  McCormick M., Wang K., Lasso A., Sharp G., Pieper S.
  DICOM Spatial Transform IO in the Insight Toolkit.
  The Insight Journal. January-December. 2014.
  https://hdl.handle.net/10380/3468
  https://www.insight-journal.org/browse/publication/923


Since ITK 4.8.0, this module is available in the ITK source tree as a Remote
module. To enable it, set::

  Module_IOTransformDCMTK:BOOL=ON

in ITK's CMake build configuration.


License
-------

This software is distributed under the Apache 2.0 license. Please see
the *LICENSE* file for details.
