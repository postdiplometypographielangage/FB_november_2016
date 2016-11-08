glyph = CurrentGlyph()

print glyph.name
print glyph.unicode
print glyph.note

# as segments
for contour in glyph:
    print contour
    for segment in contour:
        print "  ", segment
        for point in segment:
            print "    ", point.x, point.y

# as points
for contour in glyph:
    print contour
    for point in contour.points:
        print "  ", point

# as bPoints 
for contour in glyph:
    print contour
    for bPoint in contour.bPoints:
        print bPoint.bcpIn, bPoint.anchor, bPoint.bcpOut
        print         
