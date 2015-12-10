import json

def compare(a, b):
    ar = a['tpr']/(a['fpr'] + 0.000001)
    br = b['tpr']/(b['fpr'] + 0.000001)
    if ar < br:
        return 1
    elif ar > br:
        return -1
    else:
         return 0
    

with open('rates.json', 'r') as f:
    a = sorted(json.load(f), cmp=compare)
    l =  [i['cascade'] for i in a]
    for c in l[0:40]:
        print c

    
