def findLowerElevation(self, source, world):
    x, y = source
    currentRadius = 1
    maxRadius = 40
    lowestElevation = world.layers['elevation'].data[y, x]
    destination = []
    notFound = True
    isWrapped = False
    wrapped = []
    while notFound and currentRadius <= maxRadius:
        for cx in range(-currentRadius, currentRadius + 1):
            for cy in range(-currentRadius, currentRadius + 1):
                rx, ry = x + cx, y + cy
                if not self.wrap and not world.contains((rx, ry)):
                    continue
                if not in_circle(currentRadius, x, y, rx, ry):
                    continue
                rx, ry = overflow(rx, world.width), overflow(ry, world.height)
                elevation = world.layers['elevation'].data[ry, rx]
                if elevation < lowestElevation:
                    lowestElevation = elevation
                    destination = [rx, ry]
                    notFound = False
                    if not world.contains((x + cx, y + cy)):
                        wrapped.append(destination)
        currentRadius += 1
    if destination in wrapped:
        isWrapped = True
    return isWrapped, destination