def cc_to_local_params(pitch, radius, oligo):
    rloc = numpy.sin(numpy.pi / oligo) * radius
    alpha = numpy.arctan(2 * numpy.pi * radius / pitch)
    alphaloc = numpy.cos(numpy.pi / 2 - numpy.pi / oligo) * alpha
    pitchloc = 2 * numpy.pi * rloc / numpy.tan(alphaloc)
    return pitchloc, rloc, numpy.rad2deg(alphaloc)