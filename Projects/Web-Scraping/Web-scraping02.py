import requests
import bs4
res = requests.get("https://gutenberg.org/cache/epub/67646/pg67646.txt")
res.raise_for_status()
SanIgnaciopr = bs4.BeutifulSoup(res.text, 'html.parser')
elems = SanIgnaciopr.Select('title')
print(type(SanIgnaciopr))
print(len(elems))
print(str(elems))
print(elems[0].getText())