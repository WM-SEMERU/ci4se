def color(x, y):
    if x - 4 > y - 4 and -(y - 4) <= x - 4:
        return '#CDB95B'
    elif x - 4 > y - 4 and -(y - 4) > x - 4:
        return '#CD845B'
    elif x - 4 <= y - 4 and -(y - 4) <= x - 4:
        return '#57488E'
    elif x - 4 <= y - 4 and -(y - 4) > x - 4:
        return '#3B8772'
    return 'black'