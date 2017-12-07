# Created by M Tafaquh Fiddin Al Islami
# 2110151035 | 3 D4 IT B 2017
# Politeknik Elektronika Negeri Surabaya

# Nearest Neighbor

from operator import attrgetter
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

    def getMaint(self):
        return self.__maint

    def setPersons(self, persons):
        self.__persons = persons

    def getPersons(self):
        return self.__persons

    def setSafety(self, safety):
        self.__safety = safety

    def getSafety(self):
        return self.__safety

    def setLabel(self, label):
        self.__label = label

    def getLabel(self):
        return self.__label


def showGraph():
    pass
def main():
    print("Welcome to K-Nearest Neighbor created by Tafaquh")

if __name__ == '__main__':
    main()
