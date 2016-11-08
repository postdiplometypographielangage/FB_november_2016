font = CurrentFont()

glyph1 = font["A"]
glyph2 = font["B"]

print glyph1.isCompatible(glyph2)

factor = 0.7

result = glyph1 + (glyph2 - glyph1) * factor


g = font.newGlyph("result")
g.appendGlyph(result)
g.width = result.width
print result