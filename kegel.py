def kegel(code, var1, var2):
    from math import pi, sqrt
    from os import system
    clear = lambda: system('cls')
    clear()
    result = {}
    
    if code == 12: # Radius + Höhe
        result["Radius"] = var1
        result["Höhe"] = var2
        result["Seite s"] = sqrt(var1**2 + var2**2)
        result["Mantelfläche M"] = pi * var1 * result["Seite s"]
        result["Grundfläche G"] = pi * var1**2
        result["Volumen V"] = 1/3 * result["Grundfläche G"] * result["Höhe"]
        result["Oberfläche O"] = result["Mantelfläche M"] + result["Grundfläche G"]