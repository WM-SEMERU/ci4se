def tomindecstr(origin):
    degrees, minutes = tomindec(origin)
    return "%d°%f'" % (degrees, minutes)