import math


class Point():
    x = 0
    y = 0
    mass = 0
    def __init__(self, y, x, mass):
        self.x = x
        self.y = y
        self.mass = mass
    def distance_to(self, point):
        delta_x = self.x - point.x
        delta_y = self.y - point.y
        return math.hypot(delta_x, delta_y)
    def clock_angle(self, point):
        delta_x = point.x - self.x
        delta_y =  point.y  - self.y
        # rotating by 90 deg over origin: (a, b) ->(b, -a).,
        #  so tan(y/x) -> (x, -y)
        angle = math.atan2(delta_x,  - delta_y)
        if angle < 0:
            angle += 2 * math.pi
        return angle
    
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __repr__(self):
        return str((self.y, self.x, self.mass))
    
    def __lt__(self, other):
        return [self.y, self.x, self.mass] > [other.y, other.x, other.mass]

    def __lt__(self, other):
        return [self.y, self.x, self.mass] < [other.y, other.x, other.mass]



def nearest_neighbour(point, map):
    distances = []
    for other in map:
        if point == other or point.mass < other.mass:
            pass
        else:
            temp = [point.distance_to(other), point.clock_angle(other)]
            distances.append(temp)
    distances.sort()
    try:
        return distances[0]
    except IndexError:
        return None

def move_loc(point, neighbour):
    if not neighbour[1]: # N
        new_point = Point(point.y - 1, point.x, point.mass)
    elif neighbour[1] < math.pi * 0.5 : # NE
        new_point = Point(point.y - 1, point.x + 1, point.mass)
    elif neighbour[1] == math.pi * 0.5 : # E
        new_point = Point(point.y, point.x + 1, point.mass)
    elif neighbour[1] < math.pi : # SE
        new_point = Point(point.y + 1, point.x + 1, point.mass)
    elif neighbour[1] == math.pi : # S
        new_point = Point(point.y + 1, point.x, point.mass)
    elif neighbour[1] < 1.5 * math.pi : # SW
        new_point = Point(point.y + 1, point.x - 1, point.mass)
    elif neighbour[1] == 1.5 * math.pi : # W
        new_point = Point(point.y, point.x - 1, point.mass)
    else: # NW
        new_point = Point(point.y - 1, point.x - 1, point.mass)
    return new_point


def turn(current_map):
    new_map = []
    for point in current_map:
        nearest = nearest_neighbour(point, current_map)
        if nearest:
            new_point = move_loc(point, nearest)
        else:
            new_point = point
        new_map.append(new_point)
    
    for c, point in enumerate(new_map):
        for o, other in enumerate(new_map):
            if point == other and c != o:
                new_map[c].mass += new_map[o].mass
                new_map.pop(o)

    return new_map




if __name__ == "__main__":
    game =  [(0,1,2), (10,0,2)]
    game = [Point(i[0],i[1], i[2]) for i in game]
    
    while len(game) > 1:
        new_game = turn(game)
        print(game)
        if sorted(new_game) == sorted(game):
            break
        game = new_game



    
    print(game)
        
    


    