#!/usr/bin/env python

# ==========================================================================
#
#   Copyright NumFOCUS
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0.txt
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ==========================================================================

import sys
import itk

if len(sys.argv) != 6:
    print(
        "Usage: "
        + sys.argv[0]
        + " <InputFileName> <OutputFileName> <Alpha> <Beta> <Radius>"
    )
    sys.exit(1)

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]
alpha = float(sys.argv[3])
beta = float(sys.argv[4])
radiusValue = int(sys.argv[5])

Dimension = 2

PixelType = itk.ctype("unsigned char")
ImageType = itk.Image[PixelType, Dimension]

reader = itk.ImageFileReader[ImageType].New()
reader.SetFileName(inputFileName)

histogramEqualization = itk.AdaptiveHistogramEqualizationImageFilter.New(reader)
histogramEqualization.SetAlpha(alpha)
histogramEqualization.SetBeta(beta)

radius = itk.Size[Dimension]()
radius.Fill(radiusValue)
histogramEqualization.SetRadius(radius)

itk.imwrite(histogramEqualization, outputFileName)
