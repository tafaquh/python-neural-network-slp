# Created by M Tafaquh Fiddin Al Islami
# 2110151035 | 3 D4 IT B 2017
# Politeknik Elektronika Negeri Surabaya

# Neural Network Single-Layer Perceptron

from operator import attrgetter
import random
import math
import csv
import struct
import matplotlib
import matplotlib.pyplot as plt

list_data = []


class Data(object):
    def __init__(self, buying, maint, doors, persons, lug_boot, safety):
        self.__buying = buying
        self.__maint = maint
        self.__doors = doors
        self.__persons = persons
        self.__lug_boot = lug_boot
        self.__safety = safety

    def __init__(self, buying, maint, doors, persons, lug_boot, safety, label):
        self.__buying = buying
        self.__maint = maint
        self.__doors = doors
        self.__persons = persons
        self.__lug_boot = lug_boot
        self.__safety = safety
        self.__label = label

    def printValue(self):
        buyingValue = str(self.__buying)
        maintValue = str(self.__maint)
        doorsValue = str(self.__doors)
        personsValue = str(self.__persons)
        lug_bootValue = str(self.__lug_boot)
        safetyValue = str(self.__safety)
        labelValue = str(self.__label)
        return (buyingValue + "\t" + maintValue + "\t" + doorsValue + "\t"
                + personsValue + "\t" + lug_bootValue + "\t" + safetyValue +
                "\t" + labelValue)

    def setBuying(self, buying):
        self.__buying = buying
    def getBuying(self):
        return self.__buying

    def setMaint(self, maint):
        self.__maint = maint
    def getMaint(self):
        return self.__maint

    def setDoors(self, doors):
        self.__doors = doors
    def getDoors(self):
        return self.__doors

    def setPersons(self, persons):
        self.__persons = persons
    def getPersons(self):
        return self.__persons

    def setLugBoot(self, lug_boot):
        self.__lug_boot = lug_boot
    def getLugBoot(self):
        return self.__lug_boot

    def setSafety(self, safety):
        self.__safety = safety

    def getSafety(self):
        return self.__safety

    def setLabel(self, label):
        self.__label = label

    def getLabel(self):
        return self.__label

def loadData():
    with open('car.txt', 'r') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            if row:
                if(row[0] ==  'vhigh'): row[0] = 4
                elif(row[0] ==  'high'): row[0] = 3
                elif(row[0] ==  'med'): row[0] = 2
                else: row[0] = 1

                if (row[1] == 'vhigh'): row[1] = 4
                elif (row[1] == 'high'): row[1] = 3
                elif (row[1] == 'med'): row[1] = 2
                else: row[1] = 1

                if (row[2] == '5more'): row[2] = 5

                if (row[3] == 'more'): row[3] = 5

                if (row[4] == 'small'): row[4] = 1
                elif (row[4] == 'med'): row[4] = 2
                else: row[4] = 3

                if (row[5] == 'low'): row[5] = 1
                elif (row[5] == 'med'): row[5] = 2
                else: row[5] = 3

                list_data.append(Data(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
def showGraph():
    pass
def main():
    print("Welcome to K-Nearest Neighbor created by Tafaquh")
    loadData()

if __name__ == '__main__':
    main()
