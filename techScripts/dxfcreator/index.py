from dxfwrite import DXFEngine as dxf
import json

file = open('data.json', 'r')
data = file.read()
# print(data)
data = json.loads(data)
print(data)
# drawing = dxf.drawing('test.dxf')
# drawing.add(dxf.line((0, 0), (10, 0), color=7))
# drawing.add_layer('TEXTLAYER', color=2)
# drawing.add(dxf.text('Test', insert=(0, 0.2), layer='TEXTLAYER'))
# drawing.save()