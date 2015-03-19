import argparse
import cPickle as pickle
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime


def main():
    P_FILE = 'patents.p'

    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-p', '--print_out',
        help='prints the dict to the text file', action='store_true')
    parser.add_argument('-s', '--stop',
        help='stops the recusion after one iteration', action='store_true')
    parser.add_argument('-k', '--keys',
        help='prints out a specific set of keys', action='store_true')

    args = parser.parse_args()

    if args.print_out:
        d = pickle.load(open(P_FILE, 'rb'))
        print_out(d)
        return 0

    if args.keys:
        key_test(P_FILE)
        return 0


    start = datetime.now()
    print 'start: ', start


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

        print '\nstarting:', key[0]

        directory[key] = get_next_dict(key, SITE_URL, black_list)

        # breaks if param is set in args
        if args.stop:
            break


    pickle.dump(directory, open(P_FILE, 'wb'))

    finish = datetime.now()
    print '\nstart:', start
    print 'finish: ', finish

    print 'time taken to run: ', (str(finish - start))

    print_out(directory)


# takes a key, returns a dict recursively
def get_next_dict(old_key, url, black_list):

    if 'google.com/patents' in url:
        new_dict = {}


        if url[-1] != '/' and url[-5:] != '.html':
            url += '/'

        new_url = ''.join((url, old_key[1].encode('utf-8')))

        if new_url.count('.html') >1:
            new_url = new_url.replace(old_key[1], '')

        try:
            request = urllib2.urlopen(new_url)
            html = request.read()
            soup = BeautifulSoup(html)
            
            for link in soup.find_all('a'):
                if link.text in black_list or '..' in link.get('href') or '?' in link.get('href'):
                    continue
                key = (link.text, link.get('href'))
            

                last_dir = old_key[1].split('/')[0]
                next_url = new_url.replace(old_key[-1], last_dir)

                # print '\nurl: ', url
                # print 'last dir:', last_dir
                # print 'old_key[1]:', old_key[1]
                # print 'new_url before:', new_url
                # print 'next key', key[1]
                # print 'next_url:', next_url

                # '_' statement to limit page links
                # url == next_url to prevent infinite loops
                if 'http' in key[1] or key[1].count('_') > 1 or url == next_url:
                    new_dict[key] = key[1]
                else:
                    new_dict[key] = get_next_dict(key, next_url, black_list)

        except Exception as e:
            e_time = datetime.now()
            print '\n\n', e_time
            print e, ':', next_url
            return '0'
            pass

        return new_dict

    else:
        return {}


# just to print to console a specific key test
def key_test(P_FILE):

    d = pickle.load(open(P_FILE, 'rb'))

    k1 = ('A01 - Agriculture; Forestry; Animal husbandry; Hunting; Trapping; Fishing', 'Sitemap/A01.html')
    k2 = ('A01J - Manufacture of dairy products', 'A01/A01J.html')
    k3 = ('2', 'A01J_2.html')
    k4 = ('US4232703', 'http://www.google.com/patents/US4232703')

    raw_input(d[k1][k2][k3][k4])

    for k in d[k1][k2][k3]:
        raw_input(d[k1][k2][k3][k])


# prints dict keys out to file
def print_out(d):
    with open('test.txt', 'w') as t:
        for k in d:
            k_str = "".join((k[0].encode('utf-8').strip(), ' [', k[1].encode('utf-8').strip(), ']'))
            t.write(k_str)   
            t.write('\n')

            for k2 in d[k]:
                k2_str = "".join((k2[0].encode('utf-8').strip(), ' [', k2[1].encode('utf-8').strip(), ']'))
                t.write('\t')

                t.write(k2_str)
                t.write('\n')

                for k3 in d[k][k2]:
                    k3_str = "".join((k3[0].encode('utf-8').strip(), ' [', k3[1].encode('utf-8').strip(), ']'))
                    t.write('\t\t')

                    t.write(k3_str)
                    t.write('\n')

if __name__ == '__main__':
    main()
