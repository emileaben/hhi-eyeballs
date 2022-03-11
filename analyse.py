#!/usr/bin/env python
import json

with open("data.json", 'rt') as inf:
    d = json.load( inf )

for cc in d['countries']:
    hhi = 0
    #cdata = d['countries'][cc]
    #print(cc)
    if type( d['countries'][cc]['apnic'] ) != list:
        continue
    for net in d['countries'][cc]['apnic']:
        frac = net['percent']*0.01 # convert to fraction
        hhi += frac**2
    print(f"{cc} {hhi}")
