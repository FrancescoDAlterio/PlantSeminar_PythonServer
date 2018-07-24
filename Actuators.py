
import time
import _thread
from OutputWriter import OutputWriter
from DatabaseManager import DatabaseManager
import RPi.GPIO as GPIO



class Actuators():

    ValvePin = 17


    def setupWriter(self):
        ow =OutputWriter()
        ow.setup(self.ValvePin)




    def open_water(self, duration):

        if(duration >= 1 and duration <= 5):

            valve_status = GPIO.input (self.ValvePin)
            print("valve status: ",valve_status)

            #valve_status = 1  valve off
            #valve_status = 0  valve on

            if (valve_status == 0):
                return False,"Valve is already open",4

            try:
                _thread.start_new_thread(self.__open_water, (duration,))
            except:
                print("ERROR-Actuator: Unable to create a new thread")
                return False,"ERROR: Unable to create a new thread",6

            #scrivo sul database l' ora e la durata ,tabella open_water

            db = DatabaseManager ()
            valDB = db.store_open_water (duration)


            return True,"OK",duration

        else:
            return False,"No admissible value of duration",5



    def __open_water(self,dur):


        ow = OutputWriter()
        ow.pinON(self.ValvePin)
        time.sleep(dur)
        ow.pinOFF(self.ValvePin)




        return
 
