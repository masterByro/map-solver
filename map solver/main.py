import utils
import nodes
import time

GETXCHECKPOINTS = 22
FILE = 'gow2'

MAXDIST = 999
BIGNUM = 999
ROUTELENGTH = 2 + GETXCHECKPOINTS



def main():
    start_time = time.time()
    currentDist = 0

    print("Map Crusher 2000")
    map, points = utils.mapReader(FILE)
    MAPLENGTH = len(map)
    bestDist = MAXDIST
    bestRoutes = []
    route = [0]

 
    while 0 < len(route):
        if 0 < len(route) < ROUTELENGTH:
            possibleLocations = nodes.nextNodes(route, map, MAPLENGTH, currentDist, bestDist, ROUTELENGTH)
            if possibleLocations != 'NA': 
                nextLocation=possibleLocations[0]
                route.append(nextLocation[0])
                currentDist = round(currentDist + nextLocation[1], 3)
            else:
                nodes.backNode(route, map, MAPLENGTH, currentDist, bestDist, ROUTELENGTH)
                currentDist = utils.findDistance(map, route)
        if len(route) == ROUTELENGTH:
            distance = utils.findDistance(map, route)
            print(route, distance, bestDist)
            if distance <= bestDist:
                if distance < bestDist:
                    bestDist = distance
                bestRoutes.append(list(route))
                print (route, "distance:", distance)
            nodes.backNode(route, map, MAPLENGTH, currentDist, bestDist, ROUTELENGTH)
    print ("*********************************")
    print ("BEST distance:", bestDist)
    for x in bestRoutes:
        dist = utils.findDistance(map, x)
        print(x, dist)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()