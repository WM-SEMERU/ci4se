def get_angle_difference(v1, v2):
    v1 = numpy.array(v1)
    v2 = numpy.array(v2)
    angle = numpy.arccos(old_div(numpy.dot(v1, v2), numpy.sqrt(math.fsum(v1 **
        2)) * numpy.sqrt(math.fsum(v2 ** 2))))
    return math.degrees(angle)