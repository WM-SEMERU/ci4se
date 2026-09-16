def ucross(arr1, arr2, registry=None, axisa=-1, axisb=-1, axisc=-1, axis=None):
    v = np.cross(arr1, arr2, axisa=axisa, axisb=axisb, axisc=axisc, axis=axis)
    units = arr1.units * arr2.units
    arr = unyt_array(v, units, registry=registry)
    return arr