Watershed with Distance Map
===========================

.. index::
   single: WatershedWithDistanceMap

Synopsis
--------

This example illustrates how to segment an image using the watershed method
and the signed Maurer distance map.

Results
-------

.. figure:: BubbleImage.png
  :scale: 50%
  :alt: Input image

  Input image

.. figure:: SegmentWithWatershedAndDistanceMapTest01Baseline.png
  :scale: 50%
  :alt: Segmented image

  Segmented image

Input image
^^^^^^^^^^^

.. figure:: PlateauBorderXYProjection.png
  :scale: 50%
  :alt: Plateau border XY projection image

  Plateau border XY projection image

Pipeline images
^^^^^^^^^^^^^^^

.. figure:: PipelineImages.png
  :scale: 50%
  :alt: Input image, distance image and watershed segmentation image

  Input image, distance image and watershed segmentation image

.. figure:: BubbleImageSegmentedProjectionsImage.png
  :scale: 50%
  :alt: Segmented bubble projection images nipy spectral colormap

  Segmented bubble projection images nipy spectral colormap

Clean and relabel
^^^^^^^^^^^^^^^^^

.. figure:: CleanAndRelabelProjectionImages.png
  :scale: 50%
  :alt: Segmented bubble projection images after cleaning and consecutive labelling

  Segmented bubble projection images after cleaning and consecutive labelling

3D rendering
^^^^^^^^^^^^

.. figure:: BubbleImageSegmentedVolume3D.png
  :scale: 50%
  :alt: Segmented bubble 3D image

  Segmented bubble 3D image

Bubble statistics
^^^^^^^^^^^^^^^^^

.. figure:: BubbleVolumeStatsSampleTable.png
  :scale: 50%
  :alt: Bubble volume stats sample table

  Bubble volume stats sample table

.. figure:: BubbleVolumeDensityStats.png
  :scale: 50%
  :alt: Bubble volume densities

  Bubble volume densities

.. figure:: BubbleCenters.png
  :scale: 50%
  :alt: Bubble centers

  Bubble centers

Comparison
^^^^^^^^^^

.. figure:: BubbleStatsComparison.png
  :scale: 50%
  :alt: Bubble volume histogram and center location comparison

  Bubble volume histogram and center location comparison

Code
----

C++
...

.. literalinclude:: Code.cxx
   :lines: 18-

Python
......

.. literalinclude:: Code.py
   :lines: 1, 18-


Classes demonstrated
--------------------

.. breathelink:: itk::SignedMaurerDistanceMapImageFilter
.. breathelink:: itk::WatershedImageFilter
