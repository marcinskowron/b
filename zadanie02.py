import zipfile

from collections import Counter

words = []

with zipfile.ZipFile('zadanie_1_words.zip') as z:
    for file in z.namelist():
        words += (list(z.read(file).strip().lower().decode('utf-8')))

words_set = set(words)

c = Counter(words)

for i in words_set:
    print(i, c[i])