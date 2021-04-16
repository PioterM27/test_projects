"""
Wymagania:
Napisz program który będzie pytać o podanie imienia,
dodaje imię do słownika,
zapyta co chcemy zrobić :
    czy imie jest w słowniku,
    dodac do słownika,
    usunąć ze słownika,
    podać liczbę imion w słowniku,
    wypisac imiona,
    wypisać imię i jego liczbę wystąpień
    wyjść z programu
    kontynuować podawanie imion

Każdą wykonaną opcję proszę opatrzyć stosownym komunikatem

Pomyśl:
Jak wykorzystać słownik, co zrobić gdy podane imię już istnieje?
Jak policzyć liczbę imion w słowniku?
"""
dict_of_names = {'ilość imion': 0}
choice = None
sets_of_questions = ('0.Czy imie jest w słowniku',
                     '1.Dodać imie do słownika',
                     '2.Usunąc ze słownika',
                     '3.Podać liczbę imion w słowniku',
                     '4.Wypisać wszystkie imiona',
                     '5.wypisać imie i lczbe wystąpień',
                     '6.Wyjść z programu',
                     '7.kontynuiwaoc podawanie imion')

# for question in enumerate(sets_of_questions):
#     print()

while choice != 6:
    input_name = input("Podaj imię").title()
    for question in (sets_of_questions):
        print(question)
    choice = int(input("Twój wybór: "))
    if choice == 0:
        if input_name in dict_of_names.keys():
            print(f"Imie {input_name} istnieje w słowniku")
        else:
            print(f"Imię {input_name}, nie występuje w słowniku")
    elif choice == 1:
        if input_name in dict_of_names.keys():
            dict_of_names[input_name] += 1
            dict_of_names['ilość imion'] += 1
            print('istnieje już w słowniku')
        else:
            dict_of_names[input_name] = 1
            dict_of_names['ilość imion'] += 1
    elif choice == 2:
        if input_name in dict_of_names.keys():
            if dict_of_names[input_name] == 1:
                del dict_of_names[input_name]
                dict_of_names['ilość imion'] -= 1
            else:
                dict_of_names[input_name] -= 1
                dict_of_names['ilość imion'] -= 1
        else:
            print("Podane imie nie istnieje w słowniku nie można go usunąć")
    elif choice == 3:
        print(f"Aktualna ilość imion w słowniku to: {dict_of_names['ilość imion']}")
    elif choice == 4:
        for name in dict_of_names.keys():
            if name.istitle():
                print(name)

    elif choice == 5:
        if input_name in dict_of_names.keys():
            print(f"Podane imię {input_name} występuje w słowniku: {dict_of_names[input_name]} razy  ")
        else:
            print(f"Imię {input_name} nie występuje w słowniku")
    elif choice == 7:
        continue
