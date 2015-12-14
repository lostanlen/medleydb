#!/usr/bin/env python
# -*- coding: utf-8 -*-

#mix with given mixing weights

import argparse
import librosa
import csv

def load_args(filepath):
    with open(filepath, 'r') as openfile:
        reader = csv.reader(openfile, delimiter=',') 
        filepaths = []
        weights = []
        for line in reader:
            filepaths.append(line[0])
            weights.append(float(line[1]))
    return filepaths, weights


def create_mix(filepaths, weights):
    all_weighted_audio = []
    for fpath, w in zip(filepaths, weights):
        print "loading file %s" % fpath
        audio_data, sample_rate = librosa.load(fpath)
        audio_weighted = w*(audio_data)
        all_weighted_audio.append(audio_weighted)

    mix = all_weighted_audio[0]
    for weighted_audio in all_weighted_audio[1:]:
        print "mixing file..."
        mix = mix + weighted_audio

    librosa.output.write_wav("/Users/rachelbittner/Desktop/test_mix.wav", mix, sample_rate)

    return weighted_audio


def main(args):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
       description="Takes in name of multitrack then create a new mix with given volumes")
    parser.add_argument("multitrack_id",
                        type=str,
                        help="Multitrack id string")
    parser.add_argument("mixing_weights",
                        type=str,
                        help="text file with mixing weights")
    parser.add_argument("output_file",
                        type=str,
                        help="File name of output file")

    main(parser.parse_args())


