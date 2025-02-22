#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--output_path', required=False, default = "plot.png")
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# loop the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
items = items[0:10]
items.reverse()
x = []
y = []
for k,v in items:
    x.append(k)
    y.append(v)
    print(k,':',v)

if args.key == "#코로나바이러스":
    font_path = "/usr/share/fonts/truetype/unfonts-core/UnDotum.ttf"
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams["font.family"] = font_prop.get_name()
plt.bar(x, y)
plt.xlabel(args.key)
if 'en' in x:
    plt.title("Top 10 languages with the tag " + args.key + " from tweets in 2020")
elif 'US' in x:
    plt.title("Top 10 countries with the tag " + args.key + " from tweets in 2020")
plt.savefig(args.output_path)
