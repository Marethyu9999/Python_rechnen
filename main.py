def main():
    ## Importing modules
    from os import system
    from colorama import init, Fore, Back, Style

    init(autoreset=True) ## Reseting the colors every time colors are used.

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
            kreis_choice = float(input("Wähle eine Option:\n[1] Radius\n[2] Durchmesser\n[3] Umfang\n[4] Flächeninhalt\nWahl: "))
            kreis_wert = float(input("Wert: "))
            for key, value in kreisberechnung(kreis_choice, kreis_wert).items():
                print(f"{key}: {value}")
    elif options_dimensions == 2:
        clear()
        print("Figuren Wahl:\n[1] Zylinder")
        options_3d = int(input("Wahl: "))
        if options_3d == 1:
            print("Welche Daten hast du?\n[1] Radius\n[2] Höhe\n[3] Durchmesser\n[4] Umfang\n[5] Grundfläche\n[6] Mantelfläche\n[7] Oberfläche\n[8] Volumen\nZahlen von Werten die sie besitzen nehmen(Von links nach rechts. z.B 12 für Radius + Höhe oder 14 für Radius und Umfang) und sie dann in beschriebener Zahlenform eintragen.")
            zylinderchoice = int(input("Code: "))
            for key, value in zylinderrechnung(zylinderchoice).items():
                print(f"{key}: {value}")

    else:
        print("Error")
        input("")

if __name__ == "__main__":
    main()