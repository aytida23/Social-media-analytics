"""
This is the python 2.7x script for the extraction of the facebook pages data that one administers,
it can also extract data from the public pages if you provide an access token for authentication
of a valid facebook account that possess under "Reviewed App criteria for using Page Public Content
feature" by using facebook Graph API.
"""

#imporitng libraries and modules
from __future__ import print_function
import urllib2
import json
import datetime
import csv
import time

#function for requesting the url for getting the data returned from the url
def requesting_data_from_the_url(url):
    """
    Sends a request to the url and then gets the response by opening the url
    and returns the response by using read() method
    """
    request = urllib2.Request(url)
    
    http_status_code = False

    while http_status_code is False:
        #handling errors if http doesn't return success code
        try:
            response = urllib2.urlopen(request)

            #http success code is 200
            if response.getcode() == 200:
                http_status_code = True
        except Exception, e:
            #If fails to get the success code for the http then waits for few seconds and keeps trying again and again
            print("Sorry for the inconvenience we didn't receive http success code as 200,\nAnd received this error : ",e)
            time.sleep(10)
            print("Again retrying to get the response in 10 seconds...")

    return response.read()

#function for getting the requested data of facebook page
def getting_the_facebook_page_data(facebook_page_id, page_or_user_access_token):
    """
    Takes the page's id or name with its access token and return the
    specific data that we seek for from the page using facebook graph API
    """
    #setting the facebook graph API's relevant fields with its required site,page's id and page's access token
    #authentication tells that you have a valid facebook page that you administer
    site = "https://graph.facebook.com/v3.1"
    location = "/%s/posts/" % facebook_page_id
    fields = "?fields=message,created_time,type,name,id,comments.limit(0).summary(true),shares,reactions.limit(0).summary(true)"
    authentication = "&limit=100&access_token=%s" % page_or_user_access_token

    req_url = site + location + fields + authentication

    #json.loads() converts the facebook's response to a python dictionary that will be easier ahead to manipulate
    data = json.loads(requesting_data_from_the_url(req_url))
    return data


facebook_page_id = raw_input("Enter your facebook page's id or name :\n")

page_or_user_access_token = raw_input("Enter your or page's access token for authentication :\n")

print(getting_the_facebook_page_data(facebook_page_id, page_or_user_access_token))
