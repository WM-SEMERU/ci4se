def average(a, b, distance_function):
    distances = [distance_function(x, y) for x in a for y in b]
    return sum(distances) / len(distances)