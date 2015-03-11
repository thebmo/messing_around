import cPickle as pickle
import urllib2
from bs4 import BeautifulSoup

P_FILE = 'patents.p'

SITE_URL = 'http://www.google.com/patents/sitemap/en/'
current_url = SITE_URL + 'Sitemap.html'
directory = { }

url = urllib2.urlopen(current_url)
html = url.read()
soup = BeautifulSoup(html)


for link in soup.find_all('a'):
    key = (str(link.text), link.get('href'))
    directory[key] = {}

for k in directory:
    current_url = SITE_URL + str(k[1])
    print current_url
    try:
        url = urllib2.urlopen(current_url)
        html = url.read()
        soup = BeautifulSoup(html)
        
        for link in soup.find_all('a'):
            key = (link.text, link.get('href'))
            directory[k][key] = {}
    except Exception as e:
        print e
        pass
        

    
pickle.dump(directory, open(P_FILE, 'wb'))