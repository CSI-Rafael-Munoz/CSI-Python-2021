import requests
res = requests.get("https://gutenberg.org/cache/epub/67646/pg67646.txt")
res.raise_for_status()
playFile = open("All for love.text", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()