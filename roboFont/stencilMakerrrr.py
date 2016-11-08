g = CurrentGlyph()

foreground = g.getLayer("foreground")
cutter = g.getLayer("cutter")

stencil = foreground % cutter

result = g.getLayer("result")
result.clear()
result.appendGlyph(stencil)

