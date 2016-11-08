glyph = CurrentGlyph()

glyph.prepareUndo("my remove overlap")
glyph.removeOverlap()
glyph.performUndo()