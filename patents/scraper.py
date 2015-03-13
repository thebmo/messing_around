import cPickle as pickle
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime


def main():
    start = datetime.now()
    print 'start: ', start
    
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
    
    finish = datetime.now()
    print 'finish: ', finish
    
    print 'time taken to run: ', (str(finish - start))
    
    print_out(directory)


# takes a key, returns a dict
def get_next_dict(old_key, url, black_list):
    
    if 'google.com/patents' in url:
        new_dict = {}
        if url[-1] != '/':
            url += '/'
        new_url = ''.join((url, old_key[1].encode('utf-8')))
        
        try:
            request = urllib2.urlopen(new_url)
            html = request.read()
            soup = BeautifulSoup(html)
            
            for link in soup.find_all('a'):
                if link.text in black_list or '..' in link.get('href') or '?' in link.get('href'):
                    continue
                key = (link.text, link.get('href'))
                

                last_dir = old_key[1].split('/')[0]
                print 'last dir:', last_dir
                print 'old_key[1]:', old_key[1]
                print 'new_url before:', new_url
                print 'next key', key[1]

                new_url = new_url.replace(old_key[-1], last_dir)
                
                print new_url
                
                if 'http' in key[1] or key[1].count('_') > 1:
                    new_dict[key] = key[1]
                else:
                    new_dict[key] = get_next_dict(key, new_url, black_list)
        
        except Exception as e:
            print '\n\n', e, ':', new_url
            return 0
            pass

        return new_dict
    
    else:
        return {}


# prints dict keys out to file
def print_out(d):
    with open('test.txt', 'w') as t:
        for k in d:
            k_str = "".join((k[0].encode('utf-8').strip(), ' [', k[1].encode('utf-8').strip(), ']'))
            t.write(k_str)   
            t.write('\n')
            
            for k2 in d[k]:
                k2_str = "".join((k2[0].encode('utf-8').strip(), '[', k2[1].encode('utf-8').strip(), ']'))
                t.write('\t')

                t.write(k2_str)
                t.write('\n')
            
    
if __name__ == '__main__':
    main()
