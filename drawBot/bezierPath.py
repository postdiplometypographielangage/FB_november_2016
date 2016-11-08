
path = BezierPath()
# path.oval(10, 10, 100, 100)
# path.moveTo((10, 10))
# path.lineTo((10, 200))
# path.lineTo((200, 200))
# path.curveTo((200, 150), (150, 10), (10, 10))
# path.closePath()

path.text("hello", font="Helvetica", fontSize=200)

minx, miny, maxx, maxy = path.bounds()

pathWidth = maxx - minx
pathHeight = maxy - miny


translate(10, 10)
rect(minx, miny, pathWidth, pathHeight)

stroke(1, 0, 0)
fill(None)
drawPath(path)