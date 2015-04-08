import urllib2, json

def fetch_data(DEV_KEY, videoID):

    data_url = 'https://www.googleapis.com/youtube/v3/videos?id={}&key={}&part=snippet,contentDetails'.format(videoID, DEV_KEY)

    response = urllib2.urlopen(data_url)

    # Returns a dict of a list of dicts (items)
    data = json.loads(response.read())

    return data = data['items'][0]

# for key in data:
    # print key
    # print data[key]

for key in data['snippet']:
    print key
    
title = data['snippet']['title']
duration = data['contentDetails']['duration']
duration = duration.replace('PT', '')
hours = minutes = seconds = '00'

time_notation = {'H', 'M', 'S'}

for t in time_notation:
    

if 'H' in duration:
    hours = duration.split('H')[0].zfill(2)
    duration = duration.split('H')[1]
if 'M' in duration:
    minutes = duration.split('M')[0].zfill(2)
    duration = duration.split('M')[1]
if 'S' in duration:
    seconds = duration.replace('S', '').zfill(2)
        

print '{} - [{}:{}:{}]'.format(title, hours, minutes, seconds)