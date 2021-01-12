#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Point:
    # Контейнер класса родителя
    def __init__(self):
        self.__x1 = 0
        self.__y1 = 0
        self.__x2 = 0
        self.__y2 = 0

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts1 = list(map(int, line.split(';')))
        self.__x1 = parts1[0]
        self.__y1 = parts1[1]

        line = input() if prompt is None else input(prompt)
        parts2 = list(map(int, line.split(';')))
        self.__x2 = parts2[0]
        self.__y2 = parts2[1]

    # Метод изменения переменной x1 (перемещение по оси ОY)
    def set_x1(self, x):
        self.__x1 = int(x)

    # Метод изменения переменной y1 (перемещение по оси ОХ)
    def set_y1(self, y):
        self.__y1 = int(y)

    # Метод изменения переменной x2 (перемещение по оси ОY)

    def set_x2(self, x):
        self.__x2 = int(x)

    # Метод изменения переменной y2 (перемещение по оси ОХ)
    def set_y2(self, y):
        self.__y2 = int(y)

    # Метод получения переменной x1
    def get_x1(self):
        return self.__x1

    # Метод получения переменной y1
    def get_y1(self):
        return self.__y1

    # Метод получения переменной x2

    def get_x2(self):
        return self.__x2

    # Метод получения переменной y2

    def get_y2(self):
        return self.__y2
    #Расстояние от нуля первой
    def rast_at_O_first(self):
        return math.sqrt(self.get_x1() ** 2 + self.get_y1() ** 2)
    #Расстояние от нуля второй
    def rast_at_O_second(self):
        return math.sqrt(self.get_x2() ** 2 + self.get_y2() ** 2)
    #Расстояние между точками
    def rast_at_point(self):
        return math.sqrt(abs(self.get_x1() - self.get_x2()) ** 2 + abs(self.get_y1() - self.get_y2()) ** 2)
    #Перевод в полярные координаты
    def to_polar(self, x, y):
        p = math.sqrt(x ** 2 + y ** 2)
        tg = y / x
        return p, tg
    #Сравнение точек
    def srav(self):
        if self.get_x1() == self.get_x2() and self.get_y1() == self.get_y2():
            return "Точки совпадают"
        else:
            return "Точки не совпадают"

    def dispaly(self):
        print("Коориданаты 1 точки (x1;y2) ({};{})\n"
              "Коориданаты 2 точки (x2;y2) ({};{})\n"
              "Расстояние до начало коодинат 1 точки R1={}\n"
              "Расстояние до начало коодинат 2 точки R2={}\n"
              "Расстояние между точками R3={}\n"
              "Координта 1 точки в полярной системе {}\n"
              "Координта 2 точки в полярной системе {}\n"
              "Сравнение координат точек - {}".format(self.get_x1(), self.get_y1(), self.get_x2(),
                                                      self.get_y2(),
                                                      self.rast_at_O_first(), self.rast_at_O_second(),
                                                      self.rast_at_point(),
                                                      self.to_polar(self.get_x1(), self.get_y1()),
                                                      self.to_polar(self.get_x2(), self.get_y2()),
                                                      self.srav()
                                                      )
              )


if __name__ == '__main__':
    Points = Point()
    Points.read("Введите координаты точки через ; ")
    Points.dispaly()
