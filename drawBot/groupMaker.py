from random import shuffle

names = [
    "Pauline",
    "Runxi",
    "Fatima",
    "Emilios",
    "Louis",
    "Charles",
    "Martin"
]
shuffle(names)

half = int(round(len(names) / 2.0))
# print half
print ", ".join(names[:half])
print ", ".join(names[half:])

"""
Fatima, Runxi, Emilios, Martin
Pauline, Louis, Charles
"""

