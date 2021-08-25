def zylinderrechnung():
    from math import pi, sqrt
    print("Welche Daten hast du?\n[1] Radius\n[2] Höhe\n[3] Durchmesser\n[4] Umfang\n[5] Grundfläche\n[6] Mantelfläche\n[7] Oberfläche\n[8] Volumen\nZahlen von Werten die sie besitzen nehmen(Von links nach rechts. z.B 12 für Radius + Höhe oder 14 für Radius und Umfang) und sie dann in beschriebener Zahlenform eintragen.")
    choice = int(input("Werte Code: "))

    if choice == 12:  #Radius + Höhe
        radius = float(input("Radius: "))
        höhe = float(input("Höhe: "))
        durchmesser = radius*2
        umfang =  2*radius*pi
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe
    elif choice == 34:  # Höhe + Umfang
        höhe = float(input("Höhe: "))
        umfang = float(input("Umfang: "))
        radius = umfang/pi/2
        durchmesser = radius*2
        grundfläche = radius**2*pi
        mantelfläche = 2*pi*radius*höhe
        oberfläche = 2*pi*radius*(radius+höhe)
        volumen = pi*radius**2*höhe


zylinderrechnung()
input("drücken zum schließen... ")