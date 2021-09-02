from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = {7:'Красный', 2:'Желтый', 5:'Зеленый'}
    def running_method(self):
        for i in self.__color:
            print(self.__color[i])
            sleep(i)

tl = TrafficLight()

tl.running_method()