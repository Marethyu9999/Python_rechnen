print("Kreis Berechnung\nWähle was du hast:\n[1] Radius\n[2] Durchmesser\n[3] Umfang\n[4] Flächeninhalt")

choice = input("Welche Variable hast du: ")
choice = int(choice)

if choice == 1:
    var1 = input("Radius: ")
    var1 = float(var1)
    durchmesser = var1*2
    durchmesser = float(durchmesser)
    print(durchmesser)