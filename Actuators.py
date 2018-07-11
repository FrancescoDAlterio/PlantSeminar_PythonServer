
import time
from OutputWriter import OutputWriter

class Actuators():

    ValvePin = 17

    def setupWriter(self):
        ow =OutputWriter()
        ow.setup(self.ValvePin)




    def open_water(self, duration):

        if(duration >= 1 and duration <= 5):
            return self.__open_water(duration)
        else:
            return False,"ERROR: no admissible value of type"



    def __open_water(self,dur):

        ow = OutputWriter()
        ow.pinON(self.ValvePin)
        time.sleep(dur)
        ow.pinOFF(self.ValvePin)

        return True,dur
 
