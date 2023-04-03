#!/usr/bin/env python
import json
import sys

date=sys.argv[1] # as YYYY-MM-DD


with open(f"data.{date}.json", 'rt') as inf:
    d = json.load( inf )

outf_name = f"eyeball-hhi.{date}.csv"
with open(outf_name,'wt') as outf:
    for cc in d['countries']:
        hhi = 0
        #cdata = d['countries'][cc]
        #print(cc)
        if type( d['countries'][cc]['apnic'] ) != list:
            continue
        for net in d['countries'][cc]['apnic']:
            frac = net['percent']*0.01 # convert to fraction
            hhi += frac**2
        print(f"{cc},{hhi:.3f}", file=outf)

print(f"output written to {outf_name}", file=sys.stderr)
