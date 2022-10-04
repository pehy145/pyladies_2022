# ÚKOL 17 - Kámen, nůžky, papír za pomocí and, or

print("Zahrajeme si kámen, nůžky, papír")
tah_cloveka1 = input("Člověk 1: Kámen, nůžky nebo papír?")
tah_cloveka2 = input("Člověk 2: Kámen, nůžky nebo papír?")

if tah_cloveka1 == tah_cloveka2:
    print('Plichta.')
elif tah_cloveka1 == 'kámen' and tah_cloveka2 == 'nůžky' or tah_cloveka1 == 'nůžky'and tah_cloveka2 == 'papír' or tah_cloveka1 == 'papír' and tah_cloveka2 == 'kámen':
    print('Vyhrála jsi člověk 1!')
else:
    print('Vyhrál člověk 2.')

# bohužel jsem neměla k dispozici přepis tohoto programu, protože chybí v materiálech a na hodině jsem si ho nestihla zapsat, ale pokusila jsem se to udělat alespoň takto
