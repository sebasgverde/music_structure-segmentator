#!/usr/bin/env python
# coding: utf-8

# # Running MSAF #
#

"""
change the parameters as you need

Boundary methods: ['example', 'scluster', 'sf', 'vmo', 'olda', 'foote', 'cnmf']
Labeling methods: ['scluster', 'fmc2d', 'vmo', 'cnmf']

audio_file = "path_wav_file.wav"
boundaries_param = "foote"
labels_param = "cnmf"

run like this:
python segmentate.py
"""
from __future__ import print_function
import msaf
import librosa
import seaborn as sns

import run

sns.set(style="dark")


# Choose an audio file and listen to it
audio_file = '/home/sebastian/mir/strucutre_segmentation/songs/Buckethead_-_Soothsayer-adV8-_hgL4g.wav'
boundaries_param = "foote"
labels_param = "fmc2d"

output_files_name = audio_file.split("/")[-1] + "_bp_" + boundaries_param + "_lp_" + labels_param
output_file = open(output_files_name + ".txt", "wb")

# First, let's list all the available boundary algorithms
output_file.write("Boundary methods: {}".format(msaf.get_all_boundary_algorithms()))

# Let's check all the structural grouping (label) algorithms available
output_file.write("\nLabeling methods: {}".format(msaf.get_all_label_algorithms()))

# If available, you can use previously annotated boundaries and a specific labels algorithm
# Set plot = True to plot the results
# Try one of these boundary algorithms and print results
boundaries, labels = run.process(audio_file, boundaries_id=boundaries_param,
                                    labels_id=labels_param)

import datetime
time_format = [str(datetime.timedelta(seconds=int(elem))) for elem in boundaries]

boundaries = ["{:.3f}".format(elem) for elem in boundaries]


# import pdb; pdb.set_trace()
output_file.write("\n\nBoundaries: {}".format(boundaries))
output_file.write("\n\nTime Format: {}".format(time_format))
output_file.write("\n\nLabels: {}".format(labels))

output_file.write("\n\nbound, tfb, label")
for bound, tfb, label in zip (boundaries, time_format, labels):
    output_file.write("\n{} {} {}".format(bound, tfb, label))
output_file.close()
#
# output_file.write("Boundaries")
# output_file.write("\n".join(str(element) for element in boundaries))
# output_file.write("labels")
# output_file.write("\n".join(str(element) for element in labels))

# import pdb; pdb.set_trace()

# If available, you can use previously annotated boundaries and a specific labels algorithm
# Set plot = True to plot the results
boundaries, labels = run.process(audio_file, boundaries_id=boundaries_param,
                                    labels_id=labels_param, plot=True, output_file=output_files_name + ".png")
