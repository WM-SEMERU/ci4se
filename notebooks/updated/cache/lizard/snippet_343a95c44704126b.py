def uclus(a, b, distance_function):
    distances = sorted([distance_function(x, y) for x in a for y in b])
    midpoint, rest = len(distances) // 2, len(distances) % 2
    if not rest:
        return sum(distances[midpoint - 1:midpoint + 1]) / 2
    else:
        return distances[midpoint]