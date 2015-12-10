import json
import urllib
import re

u = urllib.URLopener()
u.retrieve("http://vasc.ri.cmu.edu/idb/images/face/frontal_images/list.html", "list.html")

# filename left-eye right-eye nose left-corner-mouth center-mouth right-corner-mouth
# as x y from top left

regex = r'^(\S*.gif)' + ''.join(['\s+(\d+\.?\d*)' for i in range(12)])
ground = {}

with open('list.html', 'r') as f:
    for line in f.readlines():
        if 'Rotated Test' in line:
            break

        m = re.match(regex, line)
        if m:
            fname = m.group(1)

            l_eye =   (float(m.group(2)),  float(m.group(3)))
            r_eye =   (float(m.group(4)),  float(m.group(5)))
            nose =    (float(m.group(6)),  float(m.group(7)))
            l_mouth = (float(m.group(8)),  float(m.group(9)))
            c_mouth = (float(m.group(10)), float(m.group(11)))
            r_mouth = (float(m.group(12)), float(m.group(13)))

            w = abs(2*(r_eye[0] - l_eye[0]))
            h = abs(2*(c_mouth[1] - (r_eye[1] + l_eye[1])/2))
            x = nose[0] - w/2
            y = nose[1] - h/2

            try:
                ground[fname]
            except KeyError:
                ground[fname] = [[x, y, w, h]]
            else:
                a = ground[fname]
                a.append([x, y, w, h])
                ground[fname] = a

j = []
for key in ground.keys():
    j.append({'name': key, 'ground': ground[key]})

with open('ground.json', 'w') as f:
    json.dump(j, f)
