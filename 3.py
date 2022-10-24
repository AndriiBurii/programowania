print('''Jaką operację chcesz wykonać?
1. dodawanie
2. odejmowanie
3. mnożenie
4. dzielenie
5. potęgowanie''')
oper = int(input('Wpisz numer operacji:'))
if oper > 5 or oper < 1:
    print('Niepoprawne działanie')
    exit()
arg1 = int(input('Podaj argument 1:'))
arg2 = int(input('Podaj argument 2:'))
if oper == 1:
    wynik = arg1 + arg2
elif oper == 2:
    wynik = arg1 - arg2
elif oper == 3:
    wynik = arg1 * arg2
elif oper == 4:
    if arg2 != 0:
        wynik = arg1 / arg2
    else: print('Nie dzielimy przez zero')
    exit()
else:
    wynik = arg1 ** arg2

print(f'Wynik: {wynik:.2f}')
