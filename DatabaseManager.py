import sqlite3
import time

sql_database = 'ServerDB.db'

open_water_table = 'Open_water'
owt_time = 'timestamp'
owt_duration = 'duration'

temperature_table = 'Temperature'
t_time = 'timestamp'
t_temperature = 'temperature_value'

rain_table = 'Rain'
r_time = 'timestamp'
r_rain = 'weather'

moisture_table = 'Moisture'
m_time = 'timestamp'
m_moisture = 'moisture_value'

light_table = 'Light'
l_time = 'timestamp'
l_light = 'light_value'



class DatabaseManager():


    def store_open_water(self,duration):

        return self.__store_record(0,duration)

    def store_rain(self,rain):

        return self.__store_record(1,rain)

    def store_moisture(self,moisture):

        return self.__store_record(2,moisture)

    def store_light(self,light):

        return self.__store_record(3,light)

    def store_temperature(self,temperature):

        return self.__store_record(4,temperature)


    def __store_record(self,table,specific_value):

        conn = sqlite3.connect (sql_database)
        c = conn.cursor ()

        my_time = '"' + str (time.asctime ()) + '"'


        if (table==0): #open_water
            try:
                c.execute ("INSERT INTO {tn} ({c1}, {c2}) VALUES ({tstamp}, {value})". \
                           format (tn=open_water_table, c1=owt_time, c2=owt_duration, tstamp=my_time, value=specific_value))
            except sqlite3.IntegrityError:
                conn.close ()
                return 1

        elif(table==1): #rain
            try:
                c.execute ("INSERT INTO {tn} ({c1}, {c2}) VALUES ({tstamp}, {value})". \
                           format (tn=rain_table, c1=r_time, c2=r_rain, tstamp=my_time, value=specific_value))
            except sqlite3.IntegrityError:
                conn.close ()
                return 1

        elif(table==2): #moisture
            try:
                c.execute ("INSERT INTO {tn} ({c1}, {c2}) VALUES ({tstamp}, {value})". \
                           format (tn=moisture_table, c1=m_time, c2=m_moisture, tstamp=my_time, value=specific_value))
            except sqlite3.IntegrityError:
                conn.close ()
                return 1

        elif (table == 3): #light
            try:
                c.execute ("INSERT INTO {tn} ({c1}, {c2}) VALUES ({tstamp}, {value})". \
                           format (tn=light_table, c1=l_time, c2=l_light, tstamp=my_time, value=specific_value))
            except sqlite3.IntegrityError:
                conn.close ()
                return 1

        elif (table == 4): #temperature
            try:
                c.execute ("INSERT INTO {tn} ({c1}, {c2}) VALUES ({tstamp}, {value})". \
                           format (tn=temperature_table, c1=t_time, c2=t_temperature, tstamp=my_time, value=specific_value))
            except sqlite3.IntegrityError:
                conn.close ()
                return 1

        # the else condition should do nothing, it doesn't write on the db

        conn.commit ()
        conn.close ()

        return 0

