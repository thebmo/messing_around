# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command-line skeleton application for URL Shortener API.
Usage:
  $ python sample.py

You can also get help on all the command-line flags the program understands
by running:

  $ python sample.py --help

"""

import argparse
import httplib2
import os
import sys
from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools

# # Parser for command-line arguments.
# parser = argparse.ArgumentParser(
    # description=__doc__,
    # formatter_class=argparse.RawDescriptionHelpFormatter,
    # parents=[tools.argparser])


def shorten(phenny, input):
    # CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this
    # application, including client_id and client_secret. You can see the Client ID
    # and Client secret on the APIs page in the Cloud Console:
    # <https://cloud.google.com/console#/project/266118824709/apiui>
    CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

    # Set up a Flow object to be used for authentication.
    # Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU
    # NEED. For more information on using scopes please see
    # <https://developers.google.com/+/best-practices>.
    FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,scope=['https://www.googleapis.com/auth/urlshortener'])
    # message=tools.message_if_missing(CLIENT_SECRETS))


    
    test_url = input.groups()[1]
    # print test_url
    # Parse the command-line flags.
    # flags = parser.parse_args(argv[1:])

    # If the credentials don't exist or are invalid run through the native client
    # flow. The Storage object will ensure that if successful the good
    # credentials will get written back to the file.
    storage = file.Storage('sample.dat')
    credentials = storage.get()
   
   # if credentials is None or credentials.invalid:
        # credentials = tools.run_flow(FLOW, storage)#, flags)

    # Create an httplib2.Http object to handle our HTTP requests and authorize it
    # with our good Credentials.
    http = httplib2.Http()
    # http = credentials.authorize(http)

    # Construct the service object for the interacting with the URL Shortener API.
    service = discovery.build('urlshortener', 'v1', http=http)

    try:
        url = service.url()

        # Create a shortened URL by inserting the URL into the url collection.
        body = {'longUrl': test_url }
        resp = url.insert(body=body).execute()
        # print(resp)

        short_url = resp['id']
        phenny.say(short_url)

        # Convert the shortened URL back into a long URL
        # resp = url.get(shortUrl=short_url).execute()
        # print(resp)

    except client.AccessTokenRefreshError:
        phenny.say('The credentials have been revoked')

shorten.rule = r'^(.*?)(https?://+)\b(.*)$'
        
        
      
if __name__ == '__main__': 
   print __doc__.strip()
