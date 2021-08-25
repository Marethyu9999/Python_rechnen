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

  from round2 import round2
  radius = round2(radius, 2)
  durchmesser = round2(durchmesser, 2)
  umfang = round2(umfang, 2)
  flächeninhalt = round2(flächeninhalt, 2)
  print("Ergebnis: \nRadius: " + str(radius), "\nDurchmesser: " + str(durchmesser), "\nUmfang: " + str(umfang), "\nFlächeninhalt: " + str(flächeninhalt))


