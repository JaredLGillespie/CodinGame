# https://www.codingame.com/training/easy/defibrillators


import math


def distance_between(longitudeA, latitudeA, longitudeB, latitudeB):
    x = (longitudeB - longitudeA) * math.cos((latitudeA + latitudeB) / 2)
    y = (latitudeB - latitudeA)
    return (x ** 2 + y ** 2) ** 0.5 * 6371


def solution():
    longitude = float(input().replace(',', '.'))
    latitude = float(input().replace(',', '.'))
    num_defibrillators = int(input())

    min_dist = float('inf')
    min_defib_name = None
    for _ in range(num_defibrillators):
        line = input().split(';')
        defib_longitude = float(line[4].replace(',', '.'))
        defib_latitude = float(line[5].replace(',', '.'))

        dist = distance_between(longitude, latitude, defib_longitude, defib_latitude)
        if dist < min_dist:
            min_dist = dist
            min_defib_name = line[1]

    print(min_defib_name)


solution()
