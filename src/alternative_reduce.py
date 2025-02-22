#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', required=True)
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--output_path', default="plot.png")
args = parser.parse_args()
 
# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

tags = args.hashtags.split()
data = {tag:{} for tag in tags}
# load each of the input paths
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        date = path[21:26]
        for tag in tags:
            if tag in tmp.keys():
                data[tag][date] = sum(tmp[tag].values())
            else:
                data[tag][date] = 0

font_path = "/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf"
font_prop = fm.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()

plt.figure(figsize=(11, 6))
x = list(data[tags[0]].keys())
for tag in tags:
    plt.plot(x, data[tag].values(), "-", label = tag)
x_ticks = [x[i] for i in range(0, len(x), 15)]
plt.xticks(x_ticks, rotation=45)
plt.xlabel("Days of 2020", labelpad=10, fontsize=12)
plt.ylabel("Number of tweets using the hashtag each day", labelpad=10, 
           fontsize=12)
plt.title("Trending of the hashtags during 2020 on Twitter", fontsize=14)
plt.legend()
plt.tight_layout()
plt.savefig(args.output_path, dpi=300)
