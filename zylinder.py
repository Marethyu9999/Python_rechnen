def zylinderrechnung():
    from math import pi, sqrt # Hier importiere ich module wie die Zahl pie und Quadratwurzeln
    from round2 import round2 # round2 ist kein Bänkerrunden sondern normales.

    print("Welche Daten hast du?\n[1] Radius\n[2] Höhe\n[3] Durchmesser\n[4] Umfang\n[5] Grundfläche\n[6] Mantelfläche\n[7] Oberfläche\n[8] Volumen\nZahlen von Werten die sie besitzen nehmen(Von links nach rechts. z.B 12 für Radius + Höhe oder 14 für Radius und Umfang) und sie dann in beschriebener Zahlenform eintragen.")
    choice = int(input("Code: "))

    if choice == 12:  #Radius + Höhe
        radius = float(input("Radius: "))
        höhe = float(input("Höhe: "))
        durchmesser = radius*2
        umfang =  2*pi*radius
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 16: #Radius + Mantelfläche
        radius = float(input("Radius: "))
        mantelfläche = float(input("Mantelfläche: "))
        höhe = mantelfläche/radius/pi/2
        durchmesser = radius*2
        grundfläche = radius**2*pi
        oberfläche = 2*pi*radius*(radius+höhe)
        umfang = 2*pi*radius
        volumen = pi*radius**2*höhe
    elif choice == 17: #Radius + Oberfläche
        radius = float(input("Radius: "))
        oberfläche = float(input("Oberfläche: "))
        höhe = (oberfläche-radius)/radius/pi/2
        durchmesser = radius*2
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        volumen = pi*radius**2*höhe
    elif choice == 18: #Radius + Volumen
        radius = float(input("Radius: "))
        volumen = float(input("Volumen: "))
        höhe = volumen/sqrt(radius)/pi
        durchmesser = radius*2
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        mantelfläche= 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
    elif choice == 23: #Höhe + Durchmesser
        höhe = float(input("Höhe: "))
        durchmesser = float(input("Durchmesser: "))
        radius = durchmesser/2
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 24:  # Höhe + Umfang
        höhe = float(input("Höhe: "))
        umfang = float(input("Umfang: "))
        radius = umfang/pi/2
        durchmesser = radius*2
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche =2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 25: #Höhe + Grundfläche
        höhe = float(input("Höhe: "))
        grundfläche = float(input("Grundfläche: "))
        radius = sqrt(grundfläche/pi)
        durchmesser = radius*2
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
        umfang = 2*pi*radius
        volumen = pi*radius**2*höhe
    elif choice == 26: #Höhe + Mantelfläche
        höhe = float(input("Höhe: "))
        mantelfläche = float(input("Mantelfläche: "))
        radius = 20

    else:
        print("Der eingesetzte Code ist nicht zulässig oder wird noch nicht unterstützt, probiere aber codes aus options_zylinder.txt aus da diese funktionieren werden.")


    print("Ergebnis:\nRadius: " + str(radius),"\nHöhe: " + str(höhe),"\nDurchmesser" + str(durchmesser),"\nUmfang: " + str(umfang),"\nGrundfläche: " + str(grundfläche),"\nMantelfläche: " + str(mantelfläche),"\nOberfläche: " + str(oberfläche),"\nVolumem: " + str(volumen))


zylinderrechnung()
input("drücken zum schließen... ")