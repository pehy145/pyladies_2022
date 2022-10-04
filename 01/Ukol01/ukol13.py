# ÚKOL 13 - Program, který vyhodnocuje výsledek závěrečného testu, ze kterého žáci mohli získat max. 100 bodů

body = int(input("Kolik jsi získal/a v testu bodů? "))
if body == 0:
    print("Ty jsi zapomněl/a odpovídat na otázky?")
elif body < 0:
    print("Není možné mít záporný počet bodů!")
elif body <= 10:
    print("Vůbec jsi se nesnažil, to je bohužel nedostatečné.")
elif body <= 30:
    print("To je teda s odřenýma ušima!")
elif body <= 50:
    print("Dobrý výsledek, ale příště se více snaž.")
elif body <= 70:
    print("Chválitebný výsledek, jde vidět, že jsi se připravoval/a.")
elif body <= 100:
    print("Výborný výsledek, tomu říkám dobrá práce!")
elif body > 100:
    print("Lžeš, z testu můžeš mít maximálně 100 bodů!")

else:
    print("Dělal jsi vůbec závěrečný test?")

# snažila jsem se pokrýt celou škálu, tj. záporná čísla, nulový počet bodů, jednotlivé stupnice bodů i to, kdyby člověk dostal více bodů, než je maximum