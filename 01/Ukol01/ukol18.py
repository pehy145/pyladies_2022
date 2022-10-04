# ÚKOL 18 - Program šťastná/bohatá za použití vnořeného if

print("Program, který ti napoví, jak jsi na tom v životě. Připraven/na?")
print("Odpovídej ano nebo ne (případně Ano nebo Ne)")
stastna = input("Jsi štastná?")
bohata = input("Jsi bohatá?")

if stastna == "ano" or stastna == "Ano":
    if bohata == "ano" or bohata == "Ano":
        print("Gratuluji!") # Je bohatá a zároveň šťastná
if stastna == "ano" or stastna == "Ano":
    if bohata == "ne" or bohata == "Ne":
        print("Zkus míň utrácet.") # je šťastná, není bohatá
if stastna == "ne" or stastna == "Ne":
    if bohata == "ano" or bohata == "Ano":
        print("Zkus se víc usmívat.") # není šťastná, je bohatá
if stastna == "ne" or stastna == "Ne":
    if bohata == "ne" or bohata == "Ne":
        print("To je mi líto.") # Není ani šťastná, ani bohatá

print("Díky za využití programu a přeji krásný den!")

# Zápis pomocí vnořených ifů je pro mě osobně o něco více přehledný z pohledu logiky, ale na zápis komplikovaný.