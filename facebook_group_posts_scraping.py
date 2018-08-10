"""
This is the python 2.7x script for the extraction of the facebook groups data that one administers,
it can also extract data from the public groups if you provide an user access token for authentication
of a valid facebook account that possess under "Reviewed App criteria for using 'Page Public Content
feature' by using facebook Graph API".
"""

#imporitng libraries and modules
from __future__ import print_function
import urllib2
import json
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

#function for getting the requested data of facebook group
def getting_the_facebook_page_data(facebook_group_id, user_access_token):
    """
    Takes the group's id with its user access token and return the
    specific data that we seek for from the group using facebook graph API
    """
    #setting the facebook graph API's relevant fields with its required site, group's id and user's access token
    #authentication tells that you have a valid facebook account and that you have a group that you administer
    site = "https://graph.facebook.com/v3.1"
    location = "/%s/feed/" % facebook_group_id
    fields = "?fields=message,link,created_time,type,id,comments.limit(0).summary(true),shares,reactions.limit(0).summary(true)"
    authentication = "&limit=100&access_token=%s" % user_access_token
    
    req_url = site + location + fields + authentication
    #json.loads() converts the facebook's response to a python dictionary that will be easier ahead to manipulate
    data = json.loads(requesting_data_from_the_url(req_url))
    return data


facebook_group_id = raw_input("Enter your facebook group's id or name :\n")

user_access_token = raw_input("Enter your access token for authentication :\n")
