def zylinderrechnung():
    from math import pi, sqrt # Hier importiere ich module wie die Zahl pie und Quadratwurzeln
    from os import system
    clear = lambda: system('cls')


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
        höhe = mantelfläche/(2*pi*radius)
        durchmesser = radius*2
        grundfläche = radius**2*pi
        oberfläche = 2*pi*radius*(radius+höhe)
        umfang = 2*pi*radius
        volumen = pi*radius**2*höhe
    elif choice == 17: #Radius + Oberfläche
        radius = float(input("Radius: "))
        oberfläche = float(input("Oberfläche: "))
        höhe = oberfläche/2/pi/radius-radius
        durchmesser = radius*2
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        volumen = pi*radius**2*höhe
    elif choice == 18: #Radius + Volumen
        radius = float(input("Radius: "))
        volumen = float(input("Volumen: "))
        höhe = volumen/(radius**2*pi)
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
        radius = mantelfläche/(2*pi*höhe)
        durchmesser = radius*2
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 27: #Höhe + Oberfläche
        höhe = float(input("Höhe: "))
        oberfläche = float(input("Oberfläche: "))
        radius = -höhe/2+sqrt(höhe**2/4+oberfläche/(2*pi))
        durchmesser = radius*2
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        volumen = pi*radius**2*höhe
    elif choice == 28: #Höhe + Volumen
        höhe = float(input("Höhe: "))
        volumen = float(input("Volumen: "))
        radius = sqrt(volumen/(höhe*pi))
        durchmesser = radius*2
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
    elif choice == 36: #Durchmesser + Mantelfläche
        durchmesser = float(input("Durchmesser: "))
        mantelfläche = float(input("Mantelfläche: "))
        radius = durchmesser/2
        höhe = mantelfläche/(2*pi*radius)
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 37: #Durchmesser + Oberfläche
        durchmesser = float(input("Durchmesser: "))
        oberfläche = float(input("Oberfläche: "))
        radius = durchmesser/2
        höhe = oberfläche/2/pi/radius-radius
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        volumen = pi*radius**2*höhe
    elif choice == 38: #Durchmesser + Volumen
        durchmesser = float(input("Durchmesser: "))
        volumen = float(input("Volumen: "))
        radius = durchmesser/2
        höhe = volumen/pi/sqrt(radius)
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
    elif choice == 46: #Umfang + Mantelfläche
        umfang = float(input("Umfang: "))
        mantelfläche = float(input("Mantelfläche: "))
        radius = umfang/2/pi
        höhe = mantelfläche/2/pi/radius
        durchmesser = radius*2
        grundfläche = radius**2*pi
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 47: #Umfang + Oberfläche
        umfang = float(input("Umfang: "))
        oberfläche = float(input("Oberfläche: "))
        radius = umfang/2/pi
        höhe = oberfläche/2/pi/radius-radius
        durchmesser = radius*2
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        volumen = pi*radius**2*höhe
    elif choice == 48: #Umfang + Volumen
        umfang = float(input("Umfang: "))
        volumen = float(input("Volumen: "))
        radius = umfang/2/pi
        höhe = 2*(volumen/(umfang*radius))
        durchmesser = radius*2
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
    elif choice == 56: #Grundfläche + Mantelfläche
        grundfläche = float(input("Grundfläche: "))
        mantelfläche = float(input("Mantelfläche: "))
        radius = sqrt(grundfläche/pi)
        höhe = radius*(mantelfläche/(2*grundfläche))
        durchmesser = radius*2
        umfang = 2*pi*radius
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 57: #Grundfläche + Oberfläche
        grundfläche = float(input("Grundfläche: "))
        oberfläche = float(input("Oberfläche: "))
        radius = sqrt(grundfläche/pi)
        höhe = oberfläche/2/pi/radius-radius
        durchmesser = radius*2
        umfang = 2*pi*radius
        mantelfläche = 2*pi*radius*höhe
        volumen = pi*radius**2*höhe
    elif choice == 58: #Grundfläche + Volumen
        grundfläche = float(input("Grundfläche: "))
        volumen = float(input("Volumen: "))
        radius = sqrt(grundfläche/pi)
        höhe = volumen/grundfläche
        durchmesser = radius*2
        umfang = 2*pi*radius
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 67: #Mantelfläche + Oberfläche
        mantelfläche = float(input("Mantelfläche: "))
        oberfläche = float(input("Oberfläche: "))
        höhe = sqrt(mantelfläche**2/(2*pi*oberfläche-2*pi*mantelfläche))
        radius = mantelfläche/(2*pi*höhe)
        durchmesser = radius*2
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        volumen = pi*radius**2*höhe
    elif choice == 68: #Mantelfläche + Volumen
        mantelfläche = float(input("Mantelfläche: "))
        volumen = float(input("Volumen: "))
        radius = 2*(volumen/mantelfläche)
        höhe = mantelfläche/(2*pi*radius)
        durchmesser = radius*2
        umfang = 2*pi*radius
        grundfläche = radius**2*pi
        oberfläche = 2*pi*radius*(radius+höhe)
        
    else:
        print("Der eingesetzte Code ist nicht zulässig oder wird noch nicht unterstützt.")
        input("Drücken zum schließen... ")
        exit()

    clear()
    dictornary = {"Radius":radius, "Höhe":höhe, "Durchmesser":durchmesser, "Umfang":umfang, "Grundfläche":grundfläche, "Mantelfläche":mantelfläche, "Oberfläche":oberfläche, "Volumen":volumen}
    for key, value in dictornary.items():
        print(f"{key}: {value}")