import pandas as pd
import numpy as np
import os
BIGNUM = 999

def findDistance(map, route):
        distance = 0 
        i = 0
        while i < len(route)-1:
            dist = map[int(route[i]), int(route[i+1])]
            distance += dist
            i += 1
        return round(distance, 1)

def findPoints(route, pointsList):
    totalPoints = 0
    for x in route:
        totalPoints += pointsList[x]
    return totalPoints

def distanceTooLong(map, route, MAXDIST):
        distance = 0 
        i = 0
        while i < len(route)-1:
            dist = map[int(route[i]), int(route[i+1])]
            distance += dist
            i += 1
        return distance >= MAXDIST

def mapReader(FILE): 
    script_dir = os.path.dirname(os.path.abspath(__file__))
    maps_folder = os.path.join(script_dir, 'maps')
    map = pd.read_excel(os.path.join(maps_folder, f'{FILE}.xlsx'))  ##[0,1,2][A,B,C]
    map = map.to_numpy()
    rows = len(map)
    columns = len(map[0])
    points = map[0:rows, 0]
    map = map[0:rows, 1:columns]
    columns -= 1

    i = 0
    while i < rows:
        j = 0
        while j <columns:
            if isNan(map[i][j]) and not(isNan(map[j][i])):
                map[i][j] = map[j][i]
            j += 1
        i += 1

    i = 0
    while i < rows:
        j = 0
        while j <columns:
            if map[i][j] != map[j][i] and not(isNan(map[i][j])):
                print("Error, map value mismatch: (", i, ", ", j, "), vals=" , map[i][j], ", ", map[j][i])
                quit()
            if i == j and not(isNan(map[i][j])):
                print("Error, map value at an (i,i) : (", i, ", ", j, "), val=" , map[i][j])
                quit()
            j += 1
        i += 1

    i = 0
    while i < rows:
        j = 0
        while j <columns:
            if isNan(map[i][j]):
                map[i][j] = 0
            j += 1
        i += 1
    ##print(np.matrix(map))
    return map, points

def isNan(x): 
    return (x != x)