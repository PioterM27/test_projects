"""
Zadanie z treścią:
Ania chce kupić klawiaturę k oraz pendrive p.
Posiada ustaloną kwotę pieniędzy p.
W sklepie są potane ceny w listach klawiatury i pendrivy.
Ania chce wykorzystać możliwie całą gotówkę, aby kupić klawiaturę i pendrive.


Weż pod uwagę, że Ania potrzebuje zarówno klawiatury jak i pendrive -
zakupienie jednej rzeczy nie wchodzi w grę.
Sprawdź czy uda jej się to zrobić - jeśli tak, wypisz wydaną sumę pieniędzy,
jeśli nie - podaj stosowny komunikat.

Przykładowe dane i wynik:
k = [500 ,125 ,50, 21, 13]
p = [10, 17, 28, 75]
s = 50

wynik:
Ania wydała 50zł na klawiaturę i pendrive (klawiatura kosztowała 21zł, a pendrive 28zł)
wydała 50zł na klawiaturę i pendrive (klawiatura kosztowała 21zł, a pendrive 28zł
########################################################################################################################

k = [500 ,125 ,450, 21, 66]
p = [100, 170, 30, 75]
s = 50

wynik:
Ani nie udało się zrobić zakupów za 50zł.
"""
keyboard_prices = [555, 125, 121, 450, 2, 120, 1]
pendrive_prices = [100, 120, 48, 30, 15, 11, 47]
salary = 50
keyboard_prices.sort()
pendrive_prices.sort()
min_keyboard_price = keyboard_prices[0]
available_keyboard_prices = []
available_pendrive_prices = []
pendrive = 0
keyboard = 0
diff = salary

for i, n in enumerate(keyboard_prices):
    if (n < salary):
        available_keyboard_prices.append(n)
for i, n in enumerate(pendrive_prices):
    if (n < salary and n + min_keyboard_price <= salary):
        available_pendrive_prices.append(n)
if (len(available_keyboard_prices) == 0 or len(available_pendrive_prices) == 0):
    print("Ania nie jest w stanie zakupić obu produktów")
else:
    for i in available_keyboard_prices:
        for j in available_pendrive_prices:
            if i + j <= salary and salary - (i + j) <= diff:
                keyboard = i
                pendrive = j
                diff = salary - i - j
    print(
        f"Ania wydała {salary - diff}zł na klawiaturę i pendrive (klawiatura kosztowała {keyboard}zł, a pendrive {pendrive}zł)")
