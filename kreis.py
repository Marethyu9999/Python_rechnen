def kreisberechnung():
  from math import pi, sqrt
  from os import system
  clear = lambda: system('cls')
  clear()
  print("Kreis Berechnung\nWähle was du hast:\n[1] Radius\n[2] Durchmesser\n[3] Umfang\n[4] Flächeninhalt")
  choice = input("Welche Variable hast du: ")
  choice = int(choice)

  if choice == 1:
    radius = float(input("Radius: "))
    durchmesser = radius*2
    umfang = 2*pi*radius
    flächeninhalt = radius**2*pi

  elif choice == 2:
    durchmesser = float(input("Durchmesser: "))
    radius = durchmesser/2
    umfang = 2*pi*radius
    flächeninhalt = radius**pi

  elif choice == 3:
    umfang = float(input("Umfang: "))
    radius = umfang/2/pi
    durchmesser = radius*2
    flächeninhalt = radius**pi

  elif choice == 4:
    flächeninhalt = float(input("Flächeninhalt: "))
    var1 = flächeninhalt/pi
    radius = sqrt(var1)
    durchmesser = radius*2
    umfang = 2*pi*radius
  else: 
    print("Diese Antwort ist nicht zulässig.")

  print(f"Ergebnis: \nRadius: {radius}\nDurchmesser: {durchmesser}\nUmfang: {umfang}\nFlächeninhalt: {flächeninhalt}")


