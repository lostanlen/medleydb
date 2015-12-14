#!/usr/bin/env python
# -*- coding: utf-8 -*-

#mix with given mixing weights

import argparse
import librosa

def load_args(filepath):
    with open(filepath, 'r') as openfile:
        reader = csv.reader(openfile, delimiter=',') 
        args=[]
        for line in reader:
            args.append(line)
    return args

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


