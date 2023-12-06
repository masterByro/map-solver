import utils
GETXCHECKPOINTS = 20
OUTPUTLENIENCY = 1
FILE = 'gow1'

MAXDIST = 999
BIGNUM = 999
ROUTELENGTH = 2 + GETXCHECKPOINTS



def main():
    currentDist = 0

    print("Map Crusher 2000")
    map, points = utils.mapReader(FILE)
    MAPLENGTH = len(map)
    bestDist = MAXDIST
    bestRoutes = []
    route = [0]

 
    while 0 < len(route):
        if 0 < len(route) < ROUTELENGTH:
            possibleLocations = nextNodes(route, map, MAPLENGTH, currentDist, bestDist)
            if possibleLocations != 'NA': 
                nextLocation=possibleLocations[0]
                route.append(nextLocation[0])
                currentDist = round(currentDist + nextLocation[1], 3)
            else:
                backNode(route, map, MAPLENGTH, currentDist, bestDist)
                currentDist = utils.findDistance(map, route)
        if len(route) == ROUTELENGTH:
            distance = utils.findDistance(map, route)
            print(route, distance, bestDist)
            if distance <= bestDist:
                if distance < bestDist:
                    bestDist = distance
                bestRoutes.append(list(route))
                print (route, "distance:", distance)
            backNode(route, map, MAPLENGTH, currentDist, bestDist)
    print ("*********************************")
    print ("BEST distance:", bestDist)
    for x in bestRoutes:
        dist = utils.findDistance(map, x)
        print(x, dist)

def backNode(route, map, MAPLENGTH, currentDist, bestDist):
    currentNode = route[-1]

    if len(route) > 1:
        prevNode = route[-2]
        recentDistance = map[prevNode][currentNode]
        currentDist -= recentDistance
    else:
        currentDist = 0
     
    del route[-1]
    if len(route) == 0:
        return route
    nextNodesAndDists = nextNodes(route, map, MAPLENGTH, currentDist, bestDist)
    if nextNodesAndDists != 'NA':
      possibleNextLocations = [row[0] for row in nextNodesAndDists]
      index = possibleNextLocations.index(currentNode)
    if nextNodesAndDists == 'NA' or index == len(possibleNextLocations)-1:
        backNode(route, map, MAPLENGTH, currentDist, bestDist)
    else:
        route.append(possibleNextLocations[index+1])
        return route

def nextNodes(route, map, MAPLENGTH, currentDist, bestDist):
    currentLocation = route[-1]
    distances = map[currentLocation]
    possibleNextLocations = []
    i = 0
    while i < MAPLENGTH:
        possibleDist = distances[i]
        if  not(possibleDist == 0) and not(i in route) and ( possibleDist + currentDist <= bestDist) and not(i == MAPLENGTH-1 and len(route) != ROUTELENGTH-1) and not(i != MAPLENGTH-1 and len(route) == ROUTELENGTH-1):
            possibleNextLocations.append([i,possibleDist])
            if currentDist + possibleDist >= 200:
                print(utils.findDistance(map, route))

        i += 1
    if len(possibleNextLocations) == 0: return 'NA'
    ##possibleNextLocations = sorted(possibleNextLocations, key=lambda x: x[1])
    return possibleNextLocations


if __name__ == "__main__":
    main()