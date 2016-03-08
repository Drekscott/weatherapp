__author__ = 'dreytonscott'
import smtplib
from twilio.rest import TwilioRestClient
import os
import requests
import urllib2
import json

accid = ""
auth_token = ""


def getWeather():

    url = ""
    client = TwilioRestClient(accid, auth_token)
    print ("Downloading page %s..." % url )
    response = urllib2.urlopen(url)
    data_json = response.read()
    parsed_data = json.loads(data_json)
    current_location = parsed_data['forecast']['txt_forecast']['forecastday']
    for i in range (0,2):
        day = current_location[i]['title']
        picture = current_location[i]['icon_url']
        frccast = current_location[i]['fcttext']
        frccast_metric = current_location[i]['fcttext_metric']
        picture_response = urllib2.urlopen(picture)
        weather_picture = picture_response.read()
        weather_message = client.messages.create(to="",
                            from_="",
                            body = "\n" + day + "\n" + frccast + "\n" + frccast_metric+ "\n",
                            media_url = picture)
        weather_file = open("weather_file"+str([i]), "w")
        weather_file.write(day + frccast)
        print ("File %s created" % weather_file)
        print ("Message %s created" % weather_message)
    print ("finished")
