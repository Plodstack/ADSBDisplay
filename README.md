# ADSBDisplay
ADSB display using OLED

dist_bear.py is the main script, initially it loads a reg DB of aircraft and the location of the reciever. Next a live aircraft.json is downloaded served by tar190/dump1090-fa. The list checks for location, altitude, callsign of the aircraft and calculates bearings. A aircraft type lookup for each aircraft against the reg DB, if this can't be found a registration check is attempted by lastregchk.py (this is a port using js2py and isn't readable, I couldn't translate the code by hand). 

The list is then filtered by distance/bearing (A view out the window) and number of aircraft is calculated.

The closest aircraft details and number of aircraft in view are passed to the "image_composition.py" (taken from the Luma.OLED examples) as strings. 



To do
- Source of aircraft.json to be placed into a conf file or as an argument to the script
- Window view/distance/reciever to be placed into a conf file or as an argument to the the script
- Allot more error trapping


Maybe todo 
GPSD integration - grab the reciever that way - pass this to dump1090-fa?
