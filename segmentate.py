#!/usr/bin/env python
# coding: utf-8

# # Running MSAF #
#

"""
change the parameters as you need

Boundary methods: ['example', 'scluster', 'sf', 'vmo', 'olda', 'foote', 'cnmf']
LAbeling methods: ['scluster', 'fmc2d', 'vmo', 'cnmf']

audio_file = "/home/sebastian/Downloads/20181119_paul_gilbert.wav"
boundaries_param = "foote"
labels_param = "cnmf"

run like this to conserve the metadata
 python segmentate.py > 20181119_paul_gilbert_segmentation.wav.txt

"""

from __future__ import print_function
import msaf
import librosa
import seaborn as sns

import run

sns.set(style="dark")


# Choose an audio file and listen to it
audio_file = "/home/sebastian/Downloads/20181119_paul_gilbert.wav"
boundaries_param = "foote"
labels_param = "cnmf"

output_files_name = audio_file.split("/")[-1] + "_bp_" + boundaries_param + "_lp_" + labels_param
f = open(output_files_name + ".txt", "wb")

# First, let's list all the available boundary algorithms
f.write("Boundary methods: {}".format(msaf.get_all_boundary_algorithms()))

# Let's check all the structural grouping (label) algorithms available
f.write("\nLabeling methods: {}".format(msaf.get_all_label_algorithms()))

# If available, you can use previously annotated boundaries and a specific labels algorithm
# Set plot = True to plot the results
# Try one of these boundary algorithms and print results
boundaries, labels = run.process(audio_file, boundaries_id=boundaries_param,
                                    labels_id=labels_param)

f.write("\nBoundaries: {}".format(boundaries))
f.write("\nLabels: {}".format(labels))
f.close()
#
# f.write("Boundaries")
# f.write("\n".join(str(element) for element in boundaries))
# f.write("labels")
# f.write("\n".join(str(element) for element in labels))

# import pdb; pdb.set_trace()

# If available, you can use previously annotated boundaries and a specific labels algorithm
# Set plot = True to plot the results
boundaries, labels = run.process(audio_file, boundaries_id=boundaries_param,
                                    labels_id=labels_param, plot=True, output_file=output_files_name + ".png")
