import os
import re


fLOGS = 'fred_logs.html'
tLOGS = 'temp_logs.html'
def strip_logs(fLOGS, tLOGS):
    patterns = [
        'https?.*\w',
        '\[\d+:\d+\]',
        '\[<>-:\(\)\*\^\~\]',
        'Fred Bot2',
        ]

    logs = open(fLOGS,'r').readlines()
    with open(tLOGS, 'w') as T:
        for line in logs:
            matches = []
            for p in patterns:
                matches += re.findall(p, line) 
            
            if matches:
                for match in matches:
                    line = line.replace(match, '')
                    
                    
            if line != '\n':
                T.write(line.strip(' '))
                

    os.remove(fLOGS)
    os.rename(tLOGS, fLOGS)