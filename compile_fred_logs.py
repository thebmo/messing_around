import argparse
import base64
import os
import re
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime

CWD = os.getcwd()
fLOGS = 'fred_logs.html'
tLOGS = 'temp_logs.html'
PATTERNS = [
    'https?.*\w',
    '\[\d+:\d+\]',
    '\[<>-:\(\)\*\^\~\]',
    'Fred Bot2',
    ]




def main():
    
    parser = argparse.ArgumentParser(description='Process arguments')
    parser.add_argument('-b', '--bLogs',
        help='excludes the bLogs', action='store_false')
    parser.add_argument('-e', '--eLogs',
        help='excludes the eLogs', action='store_false')
    parser.add_argument('-f', '--format',
        help='strips the patterns from the logs', action='store_false')

    args = parser.parse_args()
    
    start = datetime.now()
    print 'Starting to compile logs at: {}'.format(start)

    if args.bLogs or args.eLogs:
        if os.path.exists(os.path.join(CWD, fLOGS)):
            os.remove(fLOGS)
    
    # JMThree Log Creds
    LOGIN = os.environ['LOGS_UN']
    PWD = os.environ['LOGS_PW']
    URL = 'http://wtpa.jmthree.com/buttlog/?query=Fred'
    
    # eJohn Log Creds
    eLOGIN = os.environ['eLOGS_UN']
    ePWD = os.environ['eLOGS_PW']  
    eURL = 'http://ejohn.org/wtpa/wtpa/logs/'
     

    
    # JMThree Logs
    if args.bLogs:
        b_start = datetime.now()
        print '\nStarting JMThree logs at: {}'.format(b_start)
        
        try:
            request = urllib2.Request(URL)
            base64string = base64.encodestring('%s:%s' % (LOGIN, PWD)).replace('\n', '')
            request.add_header("Authorization", "Basic %s" % base64string)   
            results = urllib2.urlopen(request)

            html = results.read()
            results.close()
            
                

            soup = BeautifulSoup(html)

            with open(fLOGS, 'a') as logs:
 
                for line in soup.select("tr"):
                    entry = line.get_text(' ', strip=True).split(' ', 3)
                    if entry[2] == 'Fred':
                        logs.write(entry[3])
                        logs.write('\n')
                
            b_finish = datetime.now()
            print 'Finished JMThree logs at: {}'.format(b_finish)
            print 'Elapsed time for JM3 logs: {}'.format(b_finish - b_start)
            
        except urllib2.HTTPError as e:
            if '404' in e:
                print 'Too many searches, please wait a while'
            else:
               e = str(e) + ' | Search must be 4 or more characters for butt log'
               print e
            pass
    # END JM3 logs


    # eJohn Logs
    if args.eLogs:
        e_start = datetime.now()
        print '\nStarting eJohn logs at: {}'.format(e_start)
        
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
            
            with open(fLOGS, 'a') as logs:
                for match in matches:
                    clean_match = BeautifulSoup(match).get_text(' ', strip=True)
                    clean_match = clean_match.replace('<Fred> ', '')
                    logs.write(clean_match)
                    logs.write('\n')

            e_finish = datetime.now()
            print 'Finished eJohn logs at: {}'.format(e_finish)
            print 'Elapsed time for eJohn logs: {}'.format(e_finish - e_start)
            
        except Exception as e:
            e_str = ''.join(('ejohn error | ', str(e)))
            print e_str
            pass
    # End eJohn logs
    
    if args.format:
        strip_logs(fLOGS, tLOGS, PATTERNS)
    
    finish = datetime.now() 
    print '\nEnd time at: {}\nTotal elapsed time: {}'.format(finish, (finish - start))


# Strips the log of the patterns provided
def strip_logs(fLOGS, tLOGS, PATTERNS):
    
    start = datetime.now()
    print '\nStarting document stripping at: {}'.format(start)
    
    logs = open(fLOGS,'r').readlines()
    with open(tLOGS, 'w') as T:
        for line in logs:
            matches = []
            for p in PATTERNS:
                matches += re.findall(p, line) 
            
            if matches:
                for match in matches:
                    line = line.replace(match, '')
                    
                    
            if line != '\n':
                T.write(line.strip(' '))
                

    os.remove(fLOGS)
    os.rename(tLOGS, fLOGS)    
    
    finish = datetime.now()
    print 'Finished document stripping at: {}'.format(finish)
    print 'Elapsed stripping time: {}'.format(finish - start)


if __name__ == '__main__':
    main()

