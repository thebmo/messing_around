import base64
import os
import re
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime

CWD = os.getcwd()
bLOGS = 'fred_logs_butters.html'
eLOGS = 'fred_logs_ejohn.html'
tLOGS = 'temp_logs.html'

def main():
    
    start = datetime.now()
    print 'Starting to compile logs at: {}'.format(start)
    
    # # JMThree Log Creds
    # LOGIN = os.environ['LOGS_UN']
    # PWD = os.environ['LOGS_PW']
    # URL = 'http://wtpa.jmthree.com/buttlog/?query='
    # url = ''.join((URL, q))
    
    # eJohn Log Creds
    eLOGIN = os.environ['eLOGS_UN']
    ePWD = os.environ['eLOGS_PW']  
    eURL = 'http://ejohn.org/wtpa/wtpa/logs/'
     

    
    # # JMThree Logs
    # try:
        # request = urllib2.Request(url)
        # base64string = base64.encodestring('%s:%s' % (LOGIN, PWD)).replace('\n', '')
        # request.add_header("Authorization", "Basic %s" % base64string)   
        # result = urllib2.urlopen(request)

        # html = result.readline()
        # result.close()

        # soup = BeautifulSoup(html)

        # # stuffs all entries into a list
        # for line in soup.select("tr"):
            # entry = line.get_text(' ', strip=True)
            # entries.append(entry)

    # except urllib2.HTTPError as e:
        # if '404' in e:
            # phenny.say('Too many searches, please wait a while')
        # else:
           # e = str(e) + ' | Search must be 4 or more characters for butt log'
           # phenny.msg(input.nick, e)
           # # return
        # pass
    # # END JM3 logs


    
    try:
        
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, eURL, eLOGIN, ePWD)
        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)
        urllib2.install_opener(opener)
        results = urllib2.urlopen(eURL)

        html = results.read()
        results.close()
        
        freds = '&lt;Fred&gt;.*'
        matches = re.findall(freds, html)
        with open(eLOGS, 'w') as logs:
            for match in matches:
                clean_match = BeautifulSoup(match).get_text(' ', strip=True)
                clean_match = clean_match.replace('<Fred> ', '')
                logs.write(clean_match)
                logs.write('\n')

    except Exception as e:
        e_str = ''.join(('ejohn error | ', str(e)))
        print e_str
        pass
    
    
    finish = datetime.now()
    
    print 'End time at: {}\nElapsed time: {}'.format(finish, (finish - start))

if __name__ == '__main__':
    main()

