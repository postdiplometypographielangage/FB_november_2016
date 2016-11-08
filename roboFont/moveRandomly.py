from random import random

glyph = CurrentGlyph()

for contour in glyph:
    for point in contour.points:
        point.x = point.x + 10*random()-5
        point.y = point.y + 10*random()-5

glyph.update()