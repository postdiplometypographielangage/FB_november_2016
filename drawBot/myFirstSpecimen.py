# size(329, 300)
# size("A4Landscape") 
newPage("A4")


myFont = choice(installedFonts())
print myFont
myTexts = [
    "llllll",
    "lllllll",
    "abcdefghijklmnopqrstuvwxyz",
    "this is nice",
    "Typography and language",
    "AMIENS!!",
    "more text",
    "Fancy Specimen",
    "Britney!"
    ]

myTexts.reverse()

font(myFont)

for myText in myTexts:
    save()
    path = BezierPath()
    path.text(myText, font=myFont)
    minx, miny, maxx, maxy = path.bounds()
    w = maxx - minx
    h = maxy - miny
    #w, h = textSize(myText)
    s = width() / w
    # print w, h, s
    scale(s)
    # fill(random(), random(), random())
    
    t = FormattedString()
    t.font(myFont)
    for char in myText:
        t.fill(random(), random(), random())
        t.append(char)
    
    text(t, (-minx, -miny))
    restore()
    translate(0, h*s)
    


# w, h = textSize(myText)
# print w, h
# s = width() / w

# scale(s)

# text(myText, (0, 0))

# d = fontDescender()
# #    r  g  b  a
# fill(1, 0, 0, 0.5)
# rect(0, 0+d, w, h)

# newPage("A4")

# rect(10, 10, 100, 100)

