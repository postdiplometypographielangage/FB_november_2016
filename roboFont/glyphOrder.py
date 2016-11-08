from random import shuffle
font = CurrentFont()

go = font.glyphOrder
go.sort()
font.glyphOrder = go

