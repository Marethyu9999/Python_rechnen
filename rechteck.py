def quadratrechnung():
    from math import sqrt
    print("Welchen Wert möchtest du verwenden?\n[1] Seite\n[2] Umfang\n[3] Flächeninhalt")
    choice = int(input("Wert: "))

    if choice == 1:
        seite =  float(input("Seitenwert: "))
        umfang = seite*4
        fläche = seite*seite
    elif choice == 2:
        umfang = float(input("Umfang: "))
        seite =  umfang/4
        fläche = seite*seite
    elif choice == 3:
        fläche = float(input("Fläche: "))
        seite = sqrt(fläche)
        umfang = seite*4
    else:
        print("Antwort nicht gültig")
    
    print("Ergebnis:\nSeite: " + str(seite), "\nUmfang: " + str(umfang), "\nFläche: " + str(fläche))



quadratrechnung()
input("Drücke Knopf zum beenden...")