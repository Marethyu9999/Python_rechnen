from os import system

clear = lambda: system('cls')
from kreis import kreisberechnung
from zylinder import zylinderrechnung

print("Das hier ist der Launcher für das ganze Project.\nWähle eines der folgenden Optionen indem du die Zahl Schreibst.\n[1] Formen\n[2] Figuren")
options_dimensions = float(input("Wahl: "))

if options_dimensions == 1:
    clear()
    print("[1] Kreis\n[2] Viereck")
    options_2d = float(input("Wahl: "))
    if options_2d == 1:
        kreisberechnung()
        input("")
elif options_dimensions == 2:
    clear()
    print("Figuren Wahl:\n[1] Zylinder")
    options_3d = int(input("Wahl: "))
    if options_3d == 1:
        zylinderrechnung()

else:
    print("yas")
    input("")
