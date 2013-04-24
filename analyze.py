import sys
import os
from pylab import *
import collections

scenarios = ['t-mobile_android', 't-mobile_firefox', 'wired_firefox', 'wired_android', 'verizon_firefox']
sites = ['google.com', 'microsoft.com', 'amazon.com', 'cnn.com', 'twitter.com']

# indexed by (scenario, site)
dnsinfo = dict()

for sc in scenarios:
    files = os.listdir(sc)
    for file in files:
        name = file.split('_')
        if name[2] in sites:
            fname = os.path.splitext(file)[0]
            with open('dns/' + fname + '.dns2', 'r') as fhandle:
                summary = fhandle.readlines()[1:]
            
            dnsinfo[(sc, name[2])] = dict()
            contents = [line.split() for line in summary]
            ids = [c[0] for c in contents]
            #dnsinfo[(sc, name[2])]['requests'] = ids
            times = collections.defaultdict(list)
            for c in contents:
                times[c[0]].append(float(c[1]))
            
            dnsinfo[(sc, name[2])]['repeat'] = (len(ids) != len(set(ids)))

            for id in set(ids):
                dnsinfo[(sc, name[2])][id] = sum(times[id])/len(times[id])




print dnsinfo
