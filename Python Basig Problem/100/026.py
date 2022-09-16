kr_planet = ["수성", "금성", "지구", "화성", "목성", "토성", "천왕성", "해왕성"]
eg_planet = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

char = input()
if char in kr_planet:
    i = kr_planet.index(char)
    print(eg_planet[i])