class quadratischegleichung(a, b, c):
    def statecheck(a):
        # checking wich tags to apply to the formular
        states = {}
        if 0<a<1:
            states["gestaucht"] = True
        elif a>1:
            states["gestreckt"] = True
        if a<0:
            states["Richtung der Öffnung"] = "unten"
        return(states)
    
    def calculation(a,b,c,xstart,xend):
        for x in range(xstart, xend):
            a*x**2+b*x+c
    
