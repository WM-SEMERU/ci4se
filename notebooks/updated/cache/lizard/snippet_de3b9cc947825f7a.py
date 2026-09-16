def get_resampled_coordinates(lons, lats):
    num_coords = len(lons)
    assert num_coords == len(lats)
    lons1 = numpy.array(lons)
    lats1 = numpy.array(lats)
    lons2 = numpy.concatenate((lons1[1:], lons1[:1]))
    lats2 = numpy.concatenate((lats1[1:], lats1[:1]))
    distances = geodetic.geodetic_distance(lons1, lats1, lons2, lats2)
    resampled_lons = [lons[0]]
    resampled_lats = [lats[0]]
    for i in range(num_coords):
        next_point = (i + 1) % num_coords
        lon1, lat1 = lons[i], lats[i]
        lon2, lat2 = lons[next_point], lats[next_point]
        distance = distances[i]
        num_points = int(distance / UPSAMPLING_STEP_KM) + 1
        if num_points >= 2:
            new_lons, new_lats, _ = geodetic.npoints_between(lon1, lat1, 0,
                lon2, lat2, 0, num_points)
            resampled_lons.extend(new_lons[1:])
            resampled_lats.extend(new_lats[1:])
        else:
            resampled_lons.append(lon2)
            resampled_lats.append(lat2)
    return numpy.array(resampled_lons[:-1]), numpy.array(resampled_lats[:-1])