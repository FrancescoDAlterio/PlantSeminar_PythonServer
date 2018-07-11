from InputReader import InputReader

class Sensors():

    def get_soil_humidity(self):

        ir = InputReader()

        res = ir.read_analogic_sensor(1)

        return res

    def get_temperature(self):

        return 2.2

    def get_light(self):

        return 3.3





