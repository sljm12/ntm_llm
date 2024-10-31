from geojson import Feature, Polygon, MultiPolygon
from pathlib import Path
import json

c1 = [[ [99.00, 5.50], [99.00, 6.00], [99.50, 6.00], [99.50, 5.50], [99.00, 5.50]]]
c2 =[ [ [99.50, 5.50], [99.50, 5.00], [100.00, 6.00], [100.00, 5.50], [99.50, 5.50] ] ]

p = Polygon(c1)
#print(p.is_valid)
#print(p.errors())
#print(p)

f=Feature(geometry=p)
#print(f)

mp = MultiPolygon([c1,c2])
#print(mp.is_valid)
#print(mp.errors())
#print(mp)

fp = Feature(geometry=mp)
#print(fp)


text = Path("./test/PENINSULAR-NTM-206T-2024-MILITARY-EXERCISE-EKS-CARAT-24-PERAK-WATERS-.txt").read_text()
j_obj = json.loads(text)

r= []
for c in j_obj["locations"]["coordinates"]:
    r.append([c])

print(r)

mp = MultiPolygon(r)
print(mp.is_valid)
print(mp.errors())

print(Feature(geometry=mp))
'''

c11 =  [
                [
                    99,
                    5.5
                ],
                [
                    99,
                    6
                ],
                [
                    99.3,
                    6
                ],
                [
                    99.3,
                    5.5
                ],
                [
                    99,
                    5.5
                ]
            ]

c22 = [
                [
                    99.3,
                    5.5
                ],
                [
                    99.3,
                    5
                ],
                [
                    100,
                    6
                ],
                [
                    99.3,
                    6
                ],
                [
                    99.3,
                    5.5
                ]
            ]

p = MultiPolygon([[c11],[c22]])
print(p.is_valid)
print(p.errors())
f=Feature(geometry=p)
print(f)
'''