import utils
OUTPUTLENIENCY = 1
MAXDIST = 10

BIGNUM = 999


def main():
    print("Map Crusher 2000")
    map, pointsList = utils.mapReader()
    MAPLENGTH = len(map)
    bestPoints = 0
    bestPointDist = BIGNUM
    bestRoutes = []
    route = [0]

    while 0 < len(route):
        if 0 < len(route):
            possibleNextLocations = nextNodes(route, map, MAPLENGTH)
            if len(possibleNextLocations) > 0 and not utils.distanceTooLong(map, route, MAXDIST):
                route.append(possibleNextLocations[0])
            else:
                backNode(route, map, MAPLENGTH)
        if route[-1] == len(map)-1:
            distance = utils.findDistance(map, route)
            if distance <= MAXDIST:
                points = utils.findPoints(route, pointsList)
                if points > bestPoints or (points == bestPoints and distance <= bestPointDist):
                    bestPoints = points
                    bestPointDist = distance
                    bestRoutes.append(list(route))
                    print (route, "distance:", distance, "points:", points)
            backNode(route, map, MAPLENGTH)
    print ("*********************************")
    print ("BEST points:", bestPoints)
    print ("distance:", bestPointDist)
    for x in bestRoutes:
        dist = utils.findDistance(map, x)
        points = utils.findPoints(x, pointsList)
        print(x, dist, points)


def backNode(route, map, MAPLENGTH):
    currentNode = route[-1]
    del route[-1]
    if len(route) == 0:
        return route
    possibleNextLocations = nextNodes(route, map, MAPLENGTH)
    index = possibleNextLocations.index(currentNode)
    if index == len(possibleNextLocations)-1:
        backNode(route, map, MAPLENGTH)
    else:
        route.append(possibleNextLocations[index+1])
        return route

def nextNodes(route, map, MAPLENGTH):
    currentLocation = route[-1]
    distances = map[currentLocation]
    possibleNextLocations = []
    i = 0
    while i < MAPLENGTH:
        if distances[i] < BIGNUM and not(i in route):
            possibleNextLocations.append(i)
        i += 1
    return possibleNextLocations


if __name__ == "__main__":
    main()