"""
Napisz program pogodynka

Po podaniu przez uzytkownika dnia i miesiaca zaproponuj pogodę na ten dzien.
Uwzglednij:
- pore roku (np. jesienią jest zwykle deszczowo)
- temperature (przedstawiona w sopniach Farhenheita, Celcjusza i w Kelvinach)

Dla chetnych:
- uwzglednij opady
- uwzglednij stopien zachmurzenia / naslonecznienia
- uwzglednij kierunek i sile wiatru

Z gwiazdka :) - pokus sie o pobranie roku od uzytkownika i dodaj zabawny komentarz

Podpowiedzi:
Uzyj instrukcji warunkowych if/elif/else
Jesli robisz zadania dla chetnych skorzystaj z modulu random
"""

# dowolnie pobrany miesiac jako nazwe
# miesiac i dzien uwzglednic pory roku po datach kalendarzowa jesien ,lato

import random


sesons = {'Wiosna': {'pierwszy dzień': 21,
                     'miesiac': 'Marzec',
                     'temperatur': range(5, 20),
                     'pogoda': ('deszczowo', 'pochmurno', 'słonecznie', 'wietrznie')
                     },
          'Lato': {'pierwszy dzień': 22,
                   'miesiac': 'Czerwiec',
                   'temperatur': range(15, 30),
                   'pogoda': ('deszczowo', 'pochmurno', 'słonecznie', 'wietrznie', 'gorąco', 'upalnie')
                   },
          'Jesień': {
              'pierwszy dzień': 23,
              'miesiac': 'Wrzesień',
              'temperatur': range(0, 10),
              'pogoda': ('deszczowo', 'pochmurno', 'słonecznie', 'wietrznie', 'zimno', 'mgliście'),
          },
          'Zima': {
              'pierwszy dzień': 22,
              'miesiac': 'Grudzień',
              'temperatur': range(-20, 3),
              'pogoda': ('opady śniegu', 'pochmurno', 'słonecznie', 'wietrznie', 'zimno'),
          }
          }
months = {'Styczeń': {
    'ilość dni': 31,
    'pora roku': 'Zima'
},
    'Luty': {
        'ilość dni': 28,
        'pora roku': 'Zima'
    },
    'Marzec': {
        'ilość dni': 31,
        'pora roku': ''
    },
    'Kwiecień': {
        'ilość dni': 30,
        'pora roku': 'Wiosna'
    },
    'Maj': {
        'ilość dni': 31,
        'pora roku': 'Wiosna'
    },
    'Czerwiec': {
        'ilość dni': 30,
        'pora roku': ''
    },
    'Lipiec': {
        'ilość dni': 31,
        'pora roku': 'Lato'
    },
    'Sierpien': {
        'ilość dni': 31,
        'pora roku': 'Lato'
    },
    'Wrzesień': {
        'ilość dni': 30,
        'pora roku': ''
    },
    'Październik': {
        'ilość dni': 31,
        'pora roku': 'Jesień'
    },
    'Listopad': {
        'ilość dni': 30,
        'pora roku': 'Jesień'
    },
    'Grudzień': {
        'ilość dni': 31,
        'pora roku': ''
    }
}
forecast = {'dzien': 0,
            'miesiąc': '',
            'temperatura': 0,
            'jendostka': '',
            'pora roku': '',
            'pogoda': []
            }

while input_month := input("Podaj miesiac").title():
    if input_month not in months.keys():
        print("poprawny podaj")
    else:
        break
while input_day := int(input("Podaj dzien")):
    print(months[input_month])
    if months[input_month]['ilość dni'] < input_day:
        print("nie poprawny dzien")
    else:
        break
while unit := input(
        "W jakiej jednosce wyswietlić temepraturę wpisz odpowiednią literę F-Farhenheita, C-Celcjusz, K-Kelvin").title():
    if len(unit) == 1:
        break
    else:
        ("Niepoprawan forma danych")

    # Check season

if (input_month == 'Marzec'):
    forecast['pora roku'] = 'Wiosna' if input_day >= sesons['Wiosna']['pierwszy dzień'] else 'Zima'
elif ((input_month == 'Czerwiec')):
    forecast['pora roku'] = 'Lato' if input_day >= sesons['Lato']['pierwszy dzień'] else 'Wiosna'
elif (input_month == 'Wrzesień'):
    forecast['pora roku'] = 'Jesień' if input_day >= sesons['Jesień']['pierwszy dzień'] else 'Lato'
elif input_month == 'Grudzień':
    forecast['pora roku'] = 'Zima' if input_day >= sesons['Zima']['pierwszy dzień'] else 'Jesień'
else:
    forecast['pora roku'] = months[input_month]['pora roku']

current_season = forecast['pora roku']
current_temperature = random.choice(sesons[current_season]['temperatur'])
forecast['dzien'] = input_day
forecast['miesiąc'] = input_month
if unit == 'C':
    forecast['temperatura'] = current_temperature
else:
    forecast['temperatura'] = current_temperature + 273.15 if unit == 'K' else current_temperature * 1.8 + 32
forecast['jendostka'] = unit
forecast['pogoda'] = random.choice(sesons[current_season]['pogoda'])

print(f"Jest {input_day} {input_month}, aktualna pora roku to {forecast['pora roku']}.\nTemperatura w ciągu dnia "
      f"osiągnie {forecast['temperatura']} {unit}, {'Lokalnie mogą pojawić się' if forecast['pogoda'] == 'opady' else ''}"
      f"W ciągu dnia będznie {forecast['pogoda']}")