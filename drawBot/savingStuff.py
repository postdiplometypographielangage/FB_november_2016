
border = 14

txt = "abcdefghijklmnopqrstuvwxyz"
myFont = "Times"

for char in txt:
    newPage(100, 100)
    frameDuration(1)
    fill(1)
    rect(0, 0, width(), height())
    path = BezierPath()
    path.text(char, font=myFont, fontSize=100)
    
    
    fill(random(), random(), random())
    # rect(border, border, width()-    border*2, height()-border*2)
    drawPath(path)
    
saveImage("myFirstPDFfromTheScript.gif")
