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

ao=['adjectives', 'nouns']

cc1=set( dfl[ao[0]].keys() )
cc1=cc1.intersection(set( dfl[ao[1]].keys() ))

cc1 = list(cc1)

count=100
while count > 0:
    fl = random.choice(cc1)
    for j in ao:
        print(random.choice(dfl[j][fl]), end=' ')
    print()
    count -= 1



