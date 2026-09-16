def center_land(world):
    y_sums = world.layers['elevation'].data.sum(1)
    y_with_min_sum = y_sums.argmin()
    if get_verbose():
        print('geo.center_land: height complete')
    x_sums = world.layers['elevation'].data.sum(0)
    x_with_min_sum = x_sums.argmin()
    if get_verbose():
        print('geo.center_land: width complete')
    latshift = 0
    world.layers['elevation'].data = numpy.roll(numpy.roll(world.layers[
        'elevation'].data, -y_with_min_sum + latshift, axis=0), -
        x_with_min_sum, axis=1)
    world.layers['plates'].data = numpy.roll(numpy.roll(world.layers[
        'plates'].data, -y_with_min_sum + latshift, axis=0), -
        x_with_min_sum, axis=1)
    if get_verbose():
        print('geo.center_land: width complete')