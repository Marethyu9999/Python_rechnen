def main(choice, wert1, wert2):
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
    elif choice == 13: # a + ha
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
    elif choice == 14: # a + s
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
    elif choice == 18: # a + M
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
    elif choice == 19: # a + O
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
    elif choice == 110: # a + V
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
    elif choice == 23: # h + ha
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
    elif choice == 24: # h + s
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
    elif choice == 25: # h + d
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
    elif choice == 26: # h + u
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
    elif choice == 27: # h + G
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
    elif choice == 28: # h + M
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
    elif choice == 29: # h + O
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
    elif choice == 210: # h + V
        h = wert1
        V = wert2
        a = sqrt(3*V/h)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
    elif choice == 34: # ha + s
        ha = wert1
        s = wert2
        a = sqrt((-4*(ha**2))+(4*(s**2)))
        h = sqrt(ha**2-(a**2)/4)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 35: # ha + d
        ha = wert1
        d = wert2
        a = sqrt((d**2)/2)
        h = sqrt(ha**2-(a**2)/4)
        s = sqrt((h**2)+(a**2)/2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 36: # ha + u
        ha = wert1
        u = wert2
        a = u/4
        h = sqrt(ha**2-(a**2)/4)
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 37: # ha + G
        ha = wert1
        G = wert2
        a = sqrt(G)
        h = sqrt(ha**2-(a**2)/4)
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 38: # ha + M
        ha = wert1
        M = wert2
        a = M/(2*ha)
        h = sqrt(ha**2-(a**2)/4)
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 39: # ha + O
        ha = wert1
        O = wert2
        a = -ha+sqrt(ha**2+O)
        h = sqrt(ha**2-(a**2)/4)
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 45: # s + d
        s = wert1
        d = wert2
        a = sqrt((d**2)/2)
        h = sqrt((s**2)-(a**2)/2)
        ha = sqrt(h**2+((a/2)**2))
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 46: # s + u
        s = wert1
        u = wert2
        a = u/4
        h = sqrt((s**2)-(a**2)/2)
        ha = sqrt(h**2+((a/2)**2))
        d = sqrt(a**2+a**2)
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 47: # s + G
        s = wert1
        G = wert2
        a = sqrt(G)
        h = sqrt((s**2)-(a**2)/2)
        ha = sqrt(h**2+((a/2)**2))
        d = sqrt(a**2+a**2)
        u = 4*a
        M = 2*a*ha
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 48: # s + M
        s = wert1
        M = wert2
        a = sqrt(2*(s**2)-sqrt(4*(s**4)-M**2))
        h = sqrt((s**2)-(a**2)/2)
        ha = sqrt(h**2+((a/2)**2))
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 49: # s + O
        s = wert1
        O = wert2
        a = sqrt(-sqrt((-O**2)+4*O*(s**2)+4*(s**4))+O+2*(s**2))/sqrt(2)
        h = sqrt((s**2)-(a**2)/2)
        ha = sqrt(h**2+((a/2)**2))
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 58: # d + M
        d = wert1
        M = wert2
        a = sqrt((d**2)/2)
        h = sqrt((M/(2*a))**2-(a/2)**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        u = 4*a
        G = a**2
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 59: # d + O
        d = wert1
        O = wert2
        a = sqrt(d**2/2)
        h = sqrt(((O-a**2)/(2*a))**2-(a/2)**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 510: # d + V
        d = wert1
        V = wert2
        a = sqrt(d**2/2)
        h = 3*V/a**2
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        u = 4*a
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
    elif choice == 68: # u + M
        u = wert1
        M = wert2
        a = u/4
        h = sqrt((M/(2*a))**2-(a/2)**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        G = a**2
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 69: # u + O
        u = wert1
        O = wert2
        a = u/4
        h = sqrt(((O-a**2)/(2*a))**2-(a/2)**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        G = a**2
        M = 2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 610: # u + V
        u = wert1
        V = wert2
        a = u/4
        h = 3*V/a**2
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        G = a**2
        M = 2*a*ha
        O = (a**2)+2*a*ha
    elif choice == 78: # G + M
        G = wert1
        M = wert2
        a = sqrt(G)
        h = sqrt((M/(2*a))**2-(a/2)**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        O = (a**2)+2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 79: # G + O
        G = wert1
        O = wert2
        a = sqrt(G)
        h = sqrt(((O-a**2)/(2*a))**2-(a/2)**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        M = 2*a*ha
        V = (1/3)*(a**2)*h
    elif choice == 710: # G + V
        G = wert1
        V = wert2
        a = sqrt(G)
        h = 3*V/a**2
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        M = 2*a*ha
        O = (a**2)+2*a*ha
    elif choice == 89: # M + O
        M = wert1
        O = wert2
        a = sqrt(O-M)
        h = sqrt((M/(2*a))**2-(a/2)**2)
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        V = (1/3)*(a**2)*h
    elif choice == 910: # O + V
        O = wert1
        V = wert2
        a = -1/2*sqrt(O-sqrt(O*(O**3-288*V**2))/O)
        h = 3*V/a**2
        ha = sqrt(h**2+((a/2)**2))
        s = sqrt((h**2)+(a**2)/2)
        d = sqrt(a**2+a**2)
        u = 4*a
        G = a**2
        M = 2*a*ha
    


    Dictionary = {'a':a, 'h':h, 'ha':ha, 's':s, 'd':d, 'u':u, 'G':G, 'M':M, 'O':O, 'V':V}
    return Dictionary

if __name__ == '__main__':
    pyramide_choice = int(input("Wähle zwei Optionen: \n[1] Seite a\n[2]Höhe h\n[3]Höhe ha\n[4]Seitenkante s\n[5]Diagonale d\n[6]Umfang U\n[7]Grundfläche G\n[8]Mantefläche M\n[9]Oberfläche O\n[10]Volumen V\nCode: "))
    pyramide_wert1 = float(input("Wert 1: "))
    pyramide_wert2 = float(input("Wert 2: "))
    main(pyramide_choice, pyramide_wert1, pyramide_wert2)