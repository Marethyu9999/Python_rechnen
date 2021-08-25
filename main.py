from os import system

clear = lambda: system('cls')
from Kreis import kreisberechnung

print("Das hier ist der Launcher für das ganze Project.\nWähle eines der folgenden Optionen indem du die Zahl Schreibst.\n[1] 2D\n[3] 3D")
options_dimensions = float(input("Wahl: "))

if options_dimensions == 1:
    clear()
    print("[1] Kreis\n[2] Viereck")
    options_2d = float(input("Wahl: "))
    if options_2d == 1:
        kreisberechnung()
        input("")

else:
    print("yas")
    input("")
