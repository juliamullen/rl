import operator


class Path(object):
    def __init__(self, *args, **kwargs):
        self.x1         = None
        self.y1         = None
        self.x2         = None
        self.y2         = None
        self.atlas      = None
        self.directions = None

        self.state = 'unititalized'
        self.update(kwargs)

    def update(self, *args, **kwargs):
        self.x1         = kwargs.get('x1', self.x1)
        self.y1         = kwargs.get('y1', self.y1)
        self.x2         = kwargs.get('x2', self.x2)
        self.y2         = kwargs.get('y2', self.y2)
        self.atlas      = kwargs.get('atlas', self.atlas)
        self.directions = kwargs.get('directions', self.directions)
        if all((self.x1, self.y1, self.x2, self.y2, self.atlas, self.directions)):
            self.state = 'ok'

    def a_star(self):
        print "{} {} {} {}".format(self.x1, self.y1, self.x2, self.y2)
        if self.state != 'ok':
            return

        already_evaluated = set()
        to_be_evaluated = set([(self.x1, self.y1)])
        came_from = {}

        def reconstruct(came_from, current):
            total_path = [current]
            while came_from.get(current, False):
                current = came_from[current]
                total_path.append(current)
            print total_path[::-1]
            return total_path[::-1]

        g_score = {
            (self.x1, self.y1): 0,
        }

        def heuristic(x1, y1, x2, y2):
            # Manhattan metric
            manhattan = abs(x1 - x2) + abs(y1 - y2)
            return manhattan

        f_score = {
            (self.x1, self.y1): 0 + heuristic(self.x1, self.y1, self.x2, self.y2)
        }

        while to_be_evaluated:
            by_g_score = sorted(
                    [(coord, g_score.get(coord, False)) for coord in to_be_evaluated],
                    key=lambda x: x[1])
            current = by_g_score[0][0]
            if current[0] == self.x2 and current[1] == self.y2:
                return reconstruct(came_from, current)

            to_be_evaluated.remove(current)
            already_evaluated.add(current)
            for direction in self.directions.get_valid_directions(current[0], current[1], atlas=self.atlas):
                delta = direction.delta
                neighbor = (current[0] + delta[0], current[1] + delta[1])
                if neighbor in already_evaluated:
                    continue
                tentative_g = g_score[current] + 1

                if neighbor in to_be_evaluated and tentative_g >= g_score[neighbor]:
                    continue
                to_be_evaluated.add(neighbor)
                came_from[neighbor] = (current, direction)
                g_score[neighbor] = tentative_g
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor[0], neighbor[1], self.x2, self.y2)


    def get_next_step(self):
        print "going in"
        path = self.a_star()
        print "coming out"

        if path:
            print "path is {}".format(path)
            next_step = path[0]
            direction = next_step[1]
            return direction
