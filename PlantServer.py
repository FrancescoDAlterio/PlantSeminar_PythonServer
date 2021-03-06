#!/usr/bin/env python3.6

from http import client
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from io import BytesIO
from json import JSONEncoder
#import ssl
from Sensors import Sensors
from Actuators import Actuators


hostName = ""
hostPort = 4567

ac = Actuators()
ac.setupWriter()


class PlantServer (BaseHTTPRequestHandler):


    def _set_headers(self):
        #if(val):
         #   self.send_response (200)
        #else:
        #    self.send_response(422)
        self.send_response (200)
        self.send_header ('Content-type', 'application/json')
        self.end_headers ()




    #	GET is for clients geting the predi
    def do_GET(self):

        sensors = Sensors()
        # content_length = int (self.headers['Content-Length'])  # <--- Gets the size of data
        # post_data = self.rfile.read (content_length)  # <--- Gets the data itself

        response =BytesIO()

        if(self.path == '/soil_humidity'):

            s_h = sensors.get_soil_humidity()
            print (s_h)
            self._set_headers ()
            jsonString = JSONEncoder ().encode ({
                "soil_humidity": s_h,
                "time": time.asctime ()
            })
            print(jsonString)
            self.wfile.write (bytes(jsonString, "utf-8"))

        elif(self.path == '/temperature'):

            te = sensors.get_temperature()
            print (te)
            self._set_headers ()
            jsonString = JSONEncoder ().encode ({
                "temperature": te,
                "time": time.asctime ()
            })
            print (jsonString)
            self.wfile.write (bytes (jsonString, "utf-8"))

        elif (self.path == '/rain'):

            rain = sensors.get_rain()
            print (rain)
            self._set_headers ()
            jsonString = JSONEncoder ().encode ({
                "rain": rain[0],
                "rain_verbose": rain[1],
                "time": time.asctime ()
            })
            print (jsonString)
            self.wfile.write (bytes (jsonString, "utf-8"))

        elif (self.path == '/light'):

            li = sensors.get_light()
            print (li)
            self._set_headers ()
            jsonString = JSONEncoder ().encode ({
                "light": li[0],
                "condition": li[1],
                "time": time.asctime ()
            })
            print (jsonString)
            self.wfile.write (bytes (jsonString, "utf-8"))

        else:
            self.send_response (422)
            self.send_header ('Content-type', 'application/json')
            self.end_headers ()



    #	POST is for submitting data.
    def do_POST(self):



        content_length = int (self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read (content_length)  # <--- Gets the data itself
        print ("incoming http path: ", self.path, " with parameters: ",post_data)
        actuators = Actuators()

        json_post_data = {}

        if (content_length != 0):
            json_post_data = json.loads (post_data)
        #response = BytesIO ()
        data = {}

        if(self.path == '/open_water' ):

            try:
                duration =json_post_data['duration']
            except:
                print("no 'duration' entry found ")
                self._set_headers ()
                data['code'] = 2
                data['response'] = "ERROR: no 'duration' entry found"
                self.wfile.write (bytes (json.dumps (data), 'utf-8'))
                return

            try:
                duration_int = int (duration)
            except:
                print ("duration is not an integer ")
                self._set_headers ()
                data['code'] = 3
                data['response'] = "ERROR: 'duration' is not an integer"
                self.wfile.write (bytes (json.dumps (data), 'utf-8'))
                return



            res_actuator = actuators.open_water(duration_int)

            if (res_actuator[0]):
                self._set_headers ()
                data['code'] = 0
                data['time'] = time.asctime ()
                data['duration'] = res_actuator[2]
                data['response'] = res_actuator[1]


            else:

                self._set_headers ()

                #code 4=valve already open, code 5= no admissible value of duration, code 6= unable to create a thread(errore tecnico)
                data['code'] = res_actuator[2]
                data['response'] = res_actuator[1]


        else:
            self._set_headers()
            print("you are not in /open_water") #da cambiare quando lo consegni
            data['code'] = 1
            data['response'] = "ERROR: you are not in /open_water"

        print(data)
        #response.write (json.dumps(data))
        self.wfile.write (bytes (json.dumps(data), 'utf-8'))

# import pdb; pdb.set_trace()


myServer = HTTPServer ((hostName, hostPort), PlantServer)
print (time.asctime (), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever ()
except KeyboardInterrupt:
    pass

myServer.server_close ()
print (time.asctime (), "Server Stops - %s:%s" % (hostName, hostPort))


#per abilitare ssl, copia tutto prima del try
#RICORDATI DI FARE import ssl ALL INIZIO
#httpd.socket = ssl.wrap_socket (httpd.socket,
 #       keyfile="path/to/key.pem",
  #      certfile='path/to/cert.pem', server_side=True)
