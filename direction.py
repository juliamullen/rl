from pyglet.window import key

import random
random.seed()

class Direction(object):
    def __init__(self, *args, **kwargs):
        self.name  = kwargs.get('name')
        self.delta = kwargs.get('delta')

class ControlDirection(Direction):
    def __init__(self, *args, **kwargs):
        self.key = kwargs.get('key')
        _direction = kwargs.get('direction')
        if _direction:
            self.name  = _direction.name
            self.delta = _direction.delta

        super(ControlDirection, self).__init__(*args, **kwargs)

class ValidDirections(object):
    def __init__(self, *args, **kwargs):
        self.directions = kwargs.get('directions', [])

    def __iter__(self):
        return iter(self.directions)

    def get_valid_directions(self, x, y, atlas):
        """
        Returns the possible valid movement directions form (x, y)
        """
        valid_list = []

        for direction in self.directions:
            del_x, del_y = direction.delta
            if atlas.is_empty(x + del_x, y + del_y):
                valid_list.append(direction)

        return valid_list

    def get_random_direction(self, x, y, atlas):
        valid_directions = self.get_valid_directions(x, y, atlas)
        if valid_directions:
            return valid_directions[random.randint(0, len(valid_directions)-1)]
        else:
            return None


def get_standard_directions(has_controls=False):
    if has_controls:
        standard_directions = [
            ControlDirection(key=key.LEFT,  name='left',  delta=(-1, 0)),
            ControlDirection(key=key.RIGHT, name='right', delta=(1, 0)),
            ControlDirection(key=key.UP,    name='up',    delta=(0, 1)),
            ControlDirection(key=key.DOWN,  name='down',  delta=(0, -1)),
        ]
    else:
        standard_directions = [
            Direction(name='left',  delta=(-1, 0)),
            Direction(name='right', delta=(1, 0)),
            Direction(name='up',    delta=(0, 1)),
            Direction(name='down',  delta=(0, -1)),
        ]

    return ValidDirections(directions=standard_directions)


import operator

def a_star(valid_directions, x1, y1, x2, y2, atlas):
    already_evaluated = set()
    to_be_evaluated = set([(x1, y1)])
    came_from = {}

    def reconstruct(came_from, current):
        total_path = [current]
        while came_from.get(current, False):
            current = came_from[current]
            total_path.append(current)
        print total_path
        return total_path

    g_score = {
        (x1, y1): 0,
    }

    def heuristic(x1, y1, x2, y2):
        # Manhattan metric
        return abs(x1 - x2) + abs(y1 - y2)

    f_score = {
        (x1, y1): 0 + heuristic(x1, y1, x2, y2)
    }

    while to_be_evaluated:
        #print "{}{}{}{}{}".format(x1,y1,x2,y2, to_be_evaluated)
        by_g_score = sorted(
                [(coord, g_score.get(coord, False)) for coord in to_be_evaluated],
                key=lambda x: operator.itemgetter(1))
        current = by_g_score[0][0]
        #print "{} {} {}".format(current, x2, y2)
        if current[0] == x2 and current[1] == y2:
            return reconstruct(came_from, current)

        to_be_evaluated.remove(current)
        already_evaluated.add(current)
        for direction in valid_directions.get_valid_directions(current[0], current[1], atlas=atlas):
            delta = direction.delta
            neighbor = (current[0] + delta[0], current[1] + delta[1])
            if neighbor in already_evaluated:
                continue
            tentative_g = g_score[current] + 1

            if neighbor in to_be_evaluated and tentative_g >= g_score[neighbor]:
                continue
            to_be_evaluated.add(neighbor)
            came_from[neighbor] = direction
            g_score[neighbor] = tentative_g
            f_score[neighbor] = g_score[neighbor] + heuristic(neighbor[0], neighbor[1], x2, y2)
