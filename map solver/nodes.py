import utils
def nextNodes(route, map, MAPLENGTH, currentDist, bestDist, ROUTELENGTH):
    currentLocation = route[-1]
    distances = map[currentLocation]
    possibleNextLocations = []
    i = 0
    while i < MAPLENGTH:
        possibleDist = distances[i]
        if not(possibleDist == 0) and not(i in route) and ( possibleDist + currentDist <= bestDist) and not(i == MAPLENGTH-1 and len(route) != ROUTELENGTH-1) and not(i != MAPLENGTH-1 and len(route) == ROUTELENGTH-1):
            possibleNextLocations.append([i,possibleDist])
        i += 1
    if len(possibleNextLocations) == 0: return 'NA'
    return possibleNextLocations

def backNode(route, map, MAPLENGTH, currentDist, bestDist, ROUTELENGTH):
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
    nextNodesAndDists = nextNodes(route, map, MAPLENGTH, currentDist, bestDist, ROUTELENGTH)
    if nextNodesAndDists != 'NA':
      possibleNextLocations = [row[0] for row in nextNodesAndDists]
      index = possibleNextLocations.index(currentNode)
    if nextNodesAndDists == 'NA' or index == len(possibleNextLocations)-1:
        backNode(route, map, MAPLENGTH, currentDist, bestDist, ROUTELENGTH)
    else:
        route.append(possibleNextLocations[index+1])
        return route
