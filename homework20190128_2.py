import requests
import pandas as pd

address = 'https://api.spacexdata.com/v3/launches'
r = requests.get(address)
df = pd.DataFrame(r.json())