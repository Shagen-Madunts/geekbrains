"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.

"""
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        if TrafficLight.__color[0] != 'Красный' \
                or TrafficLight.__color[1] != 'Желтый' \
                or TrafficLight.__color[2] != 'Зеленый':
            print('Задан не верный режим')
        else:
            print(TrafficLight.__color[0])
            sleep(7)
            print(TrafficLight.__color[1])
            sleep(2)
            print(TrafficLight.__color[2])
            sleep(3)


instance = TrafficLight()
instance.running()
