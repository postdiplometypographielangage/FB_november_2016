fonts = AllFonts()

minFont, maxFont = fonts

factor = 3.0

dest = NewFont()
dest.interpolate(factor, minFont, maxFont, suppressError=True, analyzeOnly=False)



