ITKIOTransformDCMTK
===================

An ITK module to read DICOM spatial transforms.

.. image:: https://circleci.com/gh/InsightSoftwareConsortium/ITKIOTransformDCMTK.svg?style=svg
    :target: https://circleci.com/gh/InsightSoftwareConsortium/ITKIOTransformDCMTK

A module that extends the Insight Toolkit, `ITK <http://itk.org>`_, which
reads DICOM Spatial Rogistration Object files in itk::Transform's. Currently,
DICOM files are read by applying the DCMTK library as a backend. An
itk::DCMTKTransformIO class can be registration with the IO factory mechanism
so itk::TransformFileReadertemplate will recognize and read these files.

A more detailed description can be found in the `Insight Journal article <http://www.insight-journal.org/browse/publication/923>`_::

  McCormick M., Wang K., Lasso A., Sharp G., Pieper S. "DICOM Spatial
  Transform IO in the Insight Toolkit."
    http://hdl.handle.net/10380/3468
    http://www.insight-journal.org/browse/publication/923
    2014.

Since ITK 4.8.0, this module is available in the ITK source tree as a Remote
module.  To enable it, set::

  Module_IOTransformDCMTK:BOOL=ON

in ITK's CMake build configuration.
