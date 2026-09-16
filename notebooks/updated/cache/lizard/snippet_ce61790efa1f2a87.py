def polygonVertices(x, y, radius, sides, rotationDegrees=0,
    stretchHorizontal=1.0, stretchVertical=1.0):
    if sides % 2 == 1:
        angleOfStartPointDegrees = 90 + rotationDegrees
    else:
        angleOfStartPointDegrees = 90 + rotationDegrees - 180 / sides
    for sideNum in range(sides):
        angleOfPointRadians = math.radians(angleOfStartPointDegrees + 360 /
            sides * sideNum)
        yield int(math.cos(angleOfPointRadians) * radius * stretchHorizontal
            ) + x, -(int(math.sin(angleOfPointRadians) * radius) *
            stretchVertical) + y