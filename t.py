#! /usr/bin/env python3

import re
import random

parse = {
        'adjectives': 'Wordlist-Adjectives-Common-Audited-Len-3-6.txt',
        'nouns': 'Wordlist-Nouns-Common-Audited-Len-3-6.txt',
        }

d={}
dfl={}
for (i,j) in parse.items():
    d[i] = []
    dfl[i] = {}
    with open(j) as fh:
        for k in fh.readlines():
            k=k.strip()
            fl = k[0].lower()
            if fl not in dfl[i].keys():
                dfl[i][fl] = []
            d[i].append(k)
            dfl[i][fl].append(k)

ao=[
        ['adjectives', 'adjectives', 'nouns'],
        ['adjectives', 'nouns'],
    ]

cc1=set( dfl['adjectives'].keys() )
cc1=cc1.intersection(set( dfl['nouns'].keys() ))

cc1 = list(cc1)

count=1000
res=[]
while count > 0:
    fl = random.choice(cc1)
    for j in ao:
        s=[]
        for k in j:
            s.append(random.choice(dfl[k][fl]))
        s2 = " ".join(s)
        res.append(s2)
    count -= 1

res = sorted(res, key = lambda x: len(x))

for i in res:
    print(i)
