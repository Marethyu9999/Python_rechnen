def pyramiderechnung(choice, wert1, wert2):
    from math import sqrt

    
    if choice == 12: # a + h
        a = wert1
        h = wert2
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 13: # a + ha
        a = wert1
        ha = wert2
        h = sqrt(ha**2-((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 14: # a + s
        a = wert1
        s = wert2
        h = sqrt((s**2)-((a/2)**2))
        ha = sqrt(h**2+((a/2)**2))
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 18: # a + M
        a = wert1
        M = wert2
        h = sqrt((M/(2*a))**2-((a/2)**2))
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 19: # a + O
        a = wert1
        O = wert2
        h = sqrt(((O-a**2)/(2*a))**2-((a/2)**2))
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 110: # a + V
        a = wert1
        V = wert2
        h = (3*V)/(a**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
    if choice == 23: # h + ha
        h = wert1
        ha = wert2
        a = 2*sqrt(ha**2-h**2)
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 24: # h + s
        h = wert1
        s = wert2
        a = sqrt((2*(s**2))-(2*(h**2)))
        ha = sqrt(h**2+((a/2)**2))
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 25: # h + d
        h = wert1
        d = wert2
        a = sqrt((d**2)/2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 26: # h + u
        h = wert1
        u = wert2
        a = u/4
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 27: # h + G
        h = wert1
        G = wert2
        a = sqrt(G)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 28: # h + M
        h = wert1
        M = wert2
        a = sqrt(sqrt(4*h**4+M**2)-2*h**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    if choice == 29: # h + O
        h = wert1
        O = wert2
        a = O/sqrt(4*(h**2)+2*O)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        V = (1/3)*(a**2)*h



    Dictionary = {'a':a, 'h':h, 'ha':ha, 's':s, 'd':d, 'u':u, 'G':G, 'M':M, 'O':O, 'V':V}
    return Dictionary