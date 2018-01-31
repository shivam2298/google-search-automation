from bs4 import BeautifulSoup
import webbrowser,sys,requests

print("Searching for your queries.....")

res = requests.get("https://www.google.co.in/search?q="+''.join(sys.argv[1:]))
res.raise_for_status()
soup = BeautifulSoup(res.text)

linkelement = soup.select('.r a')


n = min(5,len(linkelement))
webbrowser.open('')
for i in range(n):
    webbrowser.open('http://google.com'+linkelement[i].get('href'),new=2)