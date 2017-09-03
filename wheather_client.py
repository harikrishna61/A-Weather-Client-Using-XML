
""""
Name-Bathala, Harikrishna
Id-1001415489
"""""
""""Beautiful soup is used in this project to parse the xml files
urlib module is used to open and request files.
"""""
from bs4 import BeautifulSoup
import urllib.request
"""request to the site is stored in the list req"""
req=urllib.request.urlopen('http://w1.weather.gov/xml/current_obs/index.xml')
"""BeautifulSoup is used to parse the xml file.the xml file is stored in the xml"""
xml= BeautifulSoup(req,'html.parser')
"""Now,the xml file is parsed and all stations are stored in the station_list list using findAll method."""
station_list=xml.findAll('station')
"""Getting the latitude and longitude  from the user."""
get_latitude=input("Enter the latitiude:")
get_longitiude=input("Enter the longitude:")
"""In this loop the stations stored in the station_list is parsed one by one and checking thr latitude and longitude
with user's ,if it matches then moving to required url"""
for item in station_list :
    """Checking the latitides and longitudes with users,and going to desired url"""
    if item.latitude.text==get_latitude and item.longitude.text==get_longitiude :
        while True :
            """"printing the name if the station name"""
            print("-----"+item.station_name.text+"------")
            """Finding the url for the xml of the or station"""
            url=item.xml_url.text
            """requesting to connect to the station."""
            req2=urllib.request.urlopen(url)
            """Now,getting the xml and parsing using BeautifulSoup"""
            wheather_details=BeautifulSoup(req2,'html.parser')
            """Finding the temperatue tag in the xml,and printing it."""
            temperature=wheather_details.findAll('temperature_string')
            for temp in temperature :
                print("Temperature:"+temp.text)
            """Finding the wind directon tag in the xml,and printing it."""
            wind_direction=wheather_details.findAll('wind_dir')
            for dir in wind_direction:
                print("Wind Direction:"+dir.text)
            """Finding the wind speed tag in the xml,and printing it."""
            wind_speed=wheather_details.findAll('wind_mph')
            for speed in wind_speed :
                print("Wind Spedd:"+speed.text)
            """Finding the dew point temperature tag in the xml,and printing it."""
            dewpoint=wheather_details.findAll('dewpoint_string')
            for dew in dewpoint :
                print("Dew Point Temperature:"+dew.text)
            refresh=input("Type yes to refresh or any key to exit: ")
            """Asking users if he wants to refresh to see anything changes ,if user says yes then requesting the url again
            and getting new values.else exiting from the program."""
            if refresh=="yes" :
                continue
            else :
                break
    else :
        print("Incorrect latitude or longtitude")
        break