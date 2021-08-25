def zylinderrechnung():
    from math import pi, sqrt # Hier importiere ich module wie die Zahl pie und Quadratwurzeln
    
    radius = 0
    höhe = 0
    durchmesser = 0
    grundfläche = 0
    mantelfläche = 0
    oberfläche = 0
    volumen = 0
    durchmesser_aus_radius = radius*2
    grundfläche_aus_radius = radius**2*pi
    mantelfläche_aus_radius = 2*pi*radius*höhe
    oberfläche_aus_radius_höhe = 2*pi*radius*(radius*höhe)
    umfang_aus_radius = 2*pi*radius
    volumen_aus_radius_höhe = pi*radius**2*höhe

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
    elif choice == 16: #Radius + Mantelfläche
        radius = float(input("Radius: "))
        mantelfläche = float(input("Mantelfläche: "))
        höhe = mantelfläche/radius/pi/2
        durchmesser = durchmesser_aus_radius
        grundfläche = grundfläche_aus_radius
        oberfläche = oberfläche_aus_radius_höhe
        umfang = umfang_aus_radius
        volumen = volumen_aus_radius_höhe
    elif choice == 34:  # Höhe + Umfang
        höhe = float(input("Höhe: "))
        umfang = float(input("Umfang: "))
        radius = umfang/pi/2
        durchmesser = radius*2
        grundfläche = radius**2*pi
        mantelfläche = mantelfläche_aus_radius
        oberfläche =oberfläche_aus_radius_höhe
        volumen = volumen_aus_radius_höhe


zylinderrechnung()
input("drücken zum schließen... ")