import os
import glob
import time

from DatabaseManager import DatabaseManager
from InputReader import InputReader

analog_pin = {
        "light": 0,
        "soil_humidity": 1,
        "rain": 2
    }

class Sensors():

    os.system ('modprobe w1-gpio')
    os.system ('modprobe w1-therm')

    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob (base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'


    def get_soil_humidity(self):
        ir = InputReader()


        res = ir.read_analogic_sensor(analog_pin["soil_humidity"])
        db = DatabaseManager ()

        if (res <= 200):
            valDB = db.store_moisture (0)
            return 0
        elif (res >=510):
            valDB = db.store_moisture (100)
            return 100
        else:
            temp = (10 * res -2000)/31
            valDB = db.store_moisture (int(temp))
            return int(temp)


    def get_light(self):
        ir = InputReader ()

        res = ir.read_analogic_sensor (analog_pin["light"])
        db = DatabaseManager ()

        if (res<=200):
            valDB = db.store_light (0)
            return 0,"Dark"
        elif(res >200 and res <= 400):
            valDB = db.store_light (1)
            return 1,"Dim" #shadow
        elif(res > 400 and res <= 700):
            valDB = db.store_light (2)
            return 2,"Light"
        elif(res >700 and res <= 900):
            valDB = db.store_light (3)
            return 3,"Bright"
        else:
            valDB = db.store_light (4)
            return 4,"Very Bright"


    def get_rain(self):
        ir = InputReader ()

        res = ir.read_analogic_sensor (analog_pin["rain"])

        db = DatabaseManager ()

        if (res > 400):
            valDB = db.store_rain (0)
            return 0,"no rain"
        elif(res >200 and res <=400):
            valDB = db.store_rain (1)
            return 1,"rain"
        else:
            valDB = db.store_rain (2)
            return 2,"heavy rain"





    def get_temperature(self):
        lines = self.__read_temp_raw ()
        if lines[0].strip ()[-3:] != 'YES':
            return -1;
        equals_pos = lines[1].find ('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            temp_c = float (temp_string) / 1000.0
            #temp_f = temp_c * 9.0 / 5.0 + 32.0
            db = DatabaseManager ()
            valDB = db.store_temperature (temp_c)

            return temp_c



    def __read_temp_raw(self):
        f = open (self.device_file, 'r')
        lines = f.readlines ()
        f.close ()
        return lines






