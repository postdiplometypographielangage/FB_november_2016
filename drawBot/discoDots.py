w = 58
h = 84

for x in range(10):
    for y in range(10):
        if (x + y) % 2:
            fill(0, 0, random())
        else:
            fill(random(), 1, 0)        
        rect(10+w*x, 10+h*y, w, h)

