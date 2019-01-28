import requests
import pandas as pd

address = 'https://api.spacexdata.com/v3/launches'
r = requests.get(address)
r_json = r.json()

ships = []
for launch in r_json:
    ships += (launch['ships'])
ships = list(set(ships))

additionalDF = []
temp = []
for ship in ships:
    for launch in r_json:
        if ship in launch['ships']:
            temp += '1'
        else:
            temp += '0'
    additionalDF.insert(-1, list(temp))

print(additionalDF)

df = pd.DataFrame(r_json)

for s in ships:
    df[s] = 0


#Korzystając z API SpaceX (https://github.com/r-spacex/SpaceX-API) odpowiedz na pytania:
#ile z wystrzeleń rakiet zakończyło się sukcesem?
#który ze statków (tych wodnych) SpaceX ma największy odsetek udanych lądowań?
#kto najczęściej korzysta z usług SpaceX do wyniesienia satelit na orbitę?
#który z klientów był najbardziej pechowy (satelity nie na orbicie)
