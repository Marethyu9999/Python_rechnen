def kreisberechnung(choice, wert):
  from math import pi, sqrt
  from os import system
  clear = lambda: system('cls')
  clear()

  if choice == 1:
    radius = wert
    durchmesser = radius*2
    umfang = 2*pi*radius
    flächeninhalt = radius**2*pi

  elif choice == 2:
    durchmesser = wert
    radius = durchmesser/2
    umfang = 2*pi*radius
    flächeninhalt = radius**pi

  elif choice == 3:
    umfang = wert
    radius = umfang/2/pi
    durchmesser = radius*2
    flächeninhalt = radius**pi

  elif choice == 4:
    flächeninhalt = wert
    var1 = flächeninhalt/pi
    radius = sqrt(var1)
    durchmesser = radius*2
    umfang = 2*pi*radius
  else: 
    print("Diese Antwort ist nicht zulässig.")

  dictionary = {"Radius": radius, "Durchmesser": durchmesser, "Umfang": umfang, "Flächeninhalt": flächeninhalt}
  return dictionary


