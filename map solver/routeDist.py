import utils

FILE = 'youyangs'
INPUT = [[0, 2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 
         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]]

def main():
    map, points = utils.mapReader(FILE)
    for route in INPUT:
        print('route: ', route, 'checkpoints: ', str(len(route) -2), 'distance: ' , utils.findDistance(map, route))
if __name__ == "__main__":
    main()