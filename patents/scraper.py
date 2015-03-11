import cPickle as pickle
import urllib2
from bs4 import BeautifulSoup

def main():
    P_FILE = 'patents.p'

    SITE_URL = 'http://www.google.com/patents/sitemap/en/'
    current_url = SITE_URL + 'Sitemap.html'
    directory = { }

    url = urllib2.urlopen(current_url)
    html = url.read()
    soup = BeautifulSoup(html)
    
    black_list = {
        'Google Home',
        'USPTO Bulk Downloads',
        'Privacy Policy',
        'Terms of Service',
        'About Google Patents',
        'Send feedback',
        'Sitemap',
        }

    for link in soup.find_all('a'):
        if link.text in black_list:
            continue
        key = (str(link.text), link.get('href'))
        directory[key] = get_next_dict(key, SITE_URL, black_list)


    pickle.dump(directory, open(P_FILE, 'wb'))
    print_out(directory)


# takes a key, returns a dict
def get_next_dict(old_key, url, black_list):
    
    new_dict = {}
    new_url = ''.join((url, str(old_key[1])))
    
    try:
        url = urllib2.urlopen(new_url)
        html = url.read()
        soup = BeautifulSoup(html)
        
        for link in soup.find_all('a'):
            if link.text in black_list:
                continue
            key = (link.text, link.get('href'))
            new_dict[key] = {}
    
    except Exception as e:
        print e, ':', new_url
        pass
    
    return new_dict


# prints dict keys out to file
def print_out(d):
    with open('test.txt', 'w') as t:
        for k in d:
            t.write(k[0].encode('utf-8').strip())
            t.write('\n')
            for k2 in d[k]:
                t.write('\t')

                t.write(k2[0].encode('utf-8').strip())
                t.write('\n')
            
    
if __name__ == '__main__':
    main()
