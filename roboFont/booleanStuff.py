font = CurrentFont()

glyph1 = font["A"]
glyph2 = font["B"]

# & --> intersection
# ^ --> xor
# % --> difference
# | --> union
result =  glyph2 | glyph1

g = font.newGlyph("result")
g.appendGlyph(result)





