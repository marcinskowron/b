from datetime import date, timedelta
from io import StringIO
import lxml.etree, lxml.html
import requests
import re
import csv

t = date(2015, 1, 1)
daty = []
for i in range(365):
    daty.append(str(t))
    t += timedelta(days=1)

dataset = []
for d in daty:
    address = 'https://www.lotto.pl/ekstra-pensja/wyniki-i-wygrane/wyszukaj'
    form_data = f'data_losowania%5Bdate%5D={d}&op=&form_build_id=form-e8e0cbce6e658bc1e8e132e4424938ff&form_id=ekstra_pensja_wyszukaj_form'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = 0
    while r != 200:
        response = requests.post(address, data=form_data, headers=headers)
        r = response.status_code
        f = StringIO(response.content.decode())
        tree = lxml.etree.parse(f, parser=lxml.etree.HTMLParser())
        results = tree.xpath("//td/div[contains(@class,'resultsItem EkstraPensja sortrosnaco')]/div/div[contains(@class,'number text-center')]/span")
        temp = [d]
        for x in results:
            temp.append(int(re.search('<span>(.+?)</span>', str(lxml.html.tostring(x))).group(1)))
        dataset.append(temp)

print(dataset)

with open('wyniki.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dataset)