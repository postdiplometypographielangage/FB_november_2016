
myText = FormattedString()

myText.fill(1, 0, 0)
myText.fontSize(100)
myText.append("hello")

myText.fill(0, 1, 0)
myText.font("Helvetica")
myText.fontSize(20)
myText.append(" world")

print myText

text(myText, (10, 10))

