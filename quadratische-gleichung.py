def quadratischegleichung(a, b, c):
    states = {}
    if 0<a<1:
        states["gestaucht"] = True
    elif a>1:
        states["gestreckt"] = True
    if a<0:
        states["Richtung der Öffnung"] = "unten"
    
    return(states)

print(quadratischegleichung(-5, 2, 3))
