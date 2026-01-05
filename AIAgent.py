import random
import math
class Searchagent:
    def __init__(self, cities):
        self.cities = cities

    def distance(self, city_A, city_B):
        dx = city_A.x - city_B.x
        dy = city_A.y - city_B.y
        return math.sqrt(dx * dx + dy * dy)

    def findway(self):
        if not self.cities:
            return []

        city_not_visited = self.cities[:]
        path = []

        # the agent also start at a random city
        current = city_not_visited[0]
        path.append(current)
        city_not_visited.remove(current)

        while city_not_visited:
            # Finding the nearest unvisited city
            citynext = min(city_not_visited, key=lambda city: self.distance(current, city))
            path.append(citynext)
            city_not_visited.remove(citynext)
            current = citynext

        path.append(path[0])

        return path