t = '''DrawBot is a powerful, free application for MacOSX that invites you to write simple Python scripts to generate two-dimensional graphics. The builtin graphics primitives support rectangles, ovals, (bezier) paths, polygons, text objects and transparency.

Education
DrawBot is an ideal tool to teach the basics of programming. Students get colorful graphic treats while getting familiar with variables, conditional statements, functions and what have you. Results can be saved in a selection of different file formats, including as high resolution, scaleable PDF, svg, movie, png, jpeg, tiff...

DrawBot has proven itself as part of the curriculum at selected courses at the Royal Academy in The Hague.

Python
DrawBot is written in Python. The binary download is fully self-contained (ie. it doesn’t need a Python install around), but the source code is available if you want to roll your own.
'''

while t:
    newPage("A4")
    fontSize(40)
    t = textBox(t, (10, 10, 300, 300))

