from geographiclib.geodesic import Geodesic
from datetime import datetime
import time
import requests
import json
from lastregchk import *
from image_composition import displayflights
# This function get the bearing and distance in metres between two GPS co-ordinates
def get_distbearing(point1,point2):
	return Geodesic.WGS84.Inverse(point1[0], point1[1], point2[0], point2[1])

# This function checks the aircraftdb for type i.e. B738, description i.e. Boeing 737-800 and it's registration
def check_aircraft(hexcode):
        hexcode = hexcode.upper()
        
        try:
                aircraft_type = aircraftdb[hexcode]['t']
                aircraft_description = aircraftdb[hexcode]['ld']
                
        except:
                aircraft_type = None
                aircraft_description = None

        try:
                aircraft_registration = aircraftdb[hexcode]['r']
        except:
                aircraft_registration = None

        if aircraft_registration == None:
                aircraft_registration = lastregchk.registration_from_hexid(hexcode)
                
        return(aircraft_type,aircraft_registration,aircraft_description)


        
# Open the aircraft information db file
print((str(datetime.now())) + ": opening the aircraft reg db")
with open('outputaircraft.json')as json_file:
        aircraftdb = json.load(json_file)
print((str(datetime.now())) + ": finished opening the aircraft reg db")


# Grab reciever location - just in case we go mobile!
print((str(datetime.now())) + ": Grabbing the reciever")
r = requests.get('http://192.168.1.242/data/receiver.json')
receiver_data = r.json()

receiver_location = receiver_data["lat"],receiver_data["lon"]
print((str(datetime.now())) + ": finished grabbing the reciever")
        #start the loop here
while True:
        # Get the list of aircraft from the json file

        print((str(datetime.now())) + ": Grabbing the aircraft list from /data/aircraft.json")
        aircraft_list_raw = requests.get('http://192.168.1.242/data/aircraft.json')
        print((str(datetime.now())) + ": Finished grabbing the list")
        aircraft_data = aircraft_list_raw.json()

        cleaned_aircraftlist  ={}
        aircraft_in_view = 0

        # start looping through the aircraft in the aircraft.json file
        for key in range(len(aircraft_data["aircraft"])):
        # Get information about the aircraft using the hexcode
            airdbdata = check_aircraft(aircraft_data["aircraft"][key]["hex"])
            aircraft_type = airdbdata[0]
            aircraft_registration = airdbdata[1]
            aircraft_description = airdbdata[2]
            # get the altitude of the aircraft
            try:
                    aircraft_altitude = aircraft_data["aircraft"][key]["alt_baro"]
            except:
                    aircraft_altitude = None
            # see if there is a callsign if not use the registration, if we can't use the registration then no callsign
            try:
                aircraft_flight = aircraft_data["aircraft"][key]["flight"]
            except:
                
                aircraft_flight = aircraft_registration
                if aircraft_flight == None:
                        aircraft_flight = "No callsign!"

            #grab the location of the aircraft
            try:

                aircraft_location = aircraft_data["aircraft"][key]["lat"],aircraft_data["aircraft"][key]["lon"]

                # compute the distance and the bearing of the aircraft
                geoinfo = get_distbearing(receiver_location,aircraft_location)
                aircraft_distance = geoinfo["s12"]/1852
                aircraft_distance = round(aircraft_distance)
                aircraft_bearing = geoinfo["azi1"]
                
                # if there is a negative bearing this needs to be corrected rounded
                if aircraft_bearing < 0:
                        aircraft_bearing = aircraft_bearing + 360

                aircraft_bearing = round(aircraft_bearing)

                # Filter out anything outside of the view of the window
                if aircraft_bearing <= 335 and aircraft_bearing >= 155:
                        aircraft_location = None

                # Filter out anything more than 20nm
                if aircraft_distance >= 200:
                        aircraft_location = None


            except:
                aircraft_location = None
                aircraft_distance = None
                aircraft_bearing = None

            # build the aircraft list we want to look at, if we can't get the location, then don't add it to the list
            if aircraft_location != None:
                        cleaned_aircraftlist.update({
                                aircraft_data["aircraft"][key]["hex"] : {
                                "callsign" : aircraft_flight.strip(),
                                "airtype" : aircraft_type,
                                "description" : aircraft_description,
                                "distance" : aircraft_distance,
                                "bearing" : aircraft_bearing,
                                "altitude" : aircraft_altitude
                                                },
                            })
                        aircraft_in_view = aircraft_in_view + 1


        # sort the list of aircraft by distance
        sorted_cleanedaircraftlist = sorted(cleaned_aircraftlist.items(), key = lambda x: x[1]["distance"])

        # loop through the closest 5 aircraft if there are less than five, it will show us what it can see...
        # unless it see nothing!
        if len(sorted_cleanedaircraftlist) != 0:
                topline = "Closest csgn: " + str(sorted_cleanedaircraftlist[0][1]['callsign'])
                topline = topline + " | Bear: " + str(sorted_cleanedaircraftlist[0][1]['bearing'])
                topline = topline + " | Dist: " + str(sorted_cleanedaircraftlist[0][1]['distance'])
                topline = topline + "nm | Alt: " + str(sorted_cleanedaircraftlist[0][1]['altitude'])
                topline = topline + "ft | Des: " + str(sorted_cleanedaircraftlist[0][1]['description'])
                displayflights(topline,"Aircraft in view: " + (str(aircraft_in_view)))
                print (topline)
                if len(sorted_cleanedaircraftlist) >= 1 and len(sorted_cleanedaircraftlist)<=5:

                       
                       for key in range(len(sorted_cleanedaircraftlist)):
                               print(sorted_cleanedaircraftlist[key])
                               
                else:

                       for key in range(5):
                               print(sorted_cleanedaircraftlist[key])
        else:
                displayflights("Nothing in view",":(")
                
        print((str(datetime.now())) + ": end. ")
