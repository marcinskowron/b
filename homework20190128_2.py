import requests
import pandas as pd

address = 'https://api.spacexdata.com/v3/launches'
r = requests.get(address)
df = pd.DataFrame(r.json())


#Korzystając z API SpaceX (https://github.com/r-spacex/SpaceX-API) odpowiedz na pytania:
#ile z wystrzeleń rakiet zakończyło się sukcesem?
#który ze statków (tych wodnych) SpaceX ma największy odsetek udanych lądowań?
#kto najczęściej korzysta z usług SpaceX do wyniesienia satelit na orbitę?
#który z klientów był najbardziej pechowy (satelity nie na orbicie)