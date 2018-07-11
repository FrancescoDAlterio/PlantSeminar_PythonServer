
#questo è uno stub per la valvola dell' acqua, ho definito 3 livelli, corrispondenti
#a tre tempi diversi, questa classe attiverà la valvola per il tempo richiesto e ritorna true
#basta solo scrivere il contenuto di open_1,2,3

#l' idea potrebbe essere anche di spawnare un thread per ogni richiesta e se il thread non ha rilasciato la critical section
#la richiesta ritorna false

class Actuators():

    def open_water(self,type):

        if(type == 1):
            return self.__open_1()
        elif(type == 2):
            return self.__open_2()
        elif(type == 3):
            return self.__open_3()
        else:
            return False,"ERROR: no admissible value of type"



    def __open_1(self):

        return True,1

    def __open_2(self):

        return True,2

    def __open_3(self):

        return True,3