def cube(data, xcoords=None, ycoords=None, chcoords=None, scalarcoords=None,
    datacoords=None, attrs=None, name=None):
    cube = xr.DataArray(data, dims=('x', 'y', 'ch'), attrs=attrs, name=name)
    cube.dcc._initcoords()
    if xcoords is not None:
        cube.coords.update({key: ('x', xcoords[key]) for key in xcoords})
    if ycoords is not None:
        cube.coords.update({key: ('y', ycoords[key]) for key in ycoords})
    if chcoords is not None:
        cube.coords.update({key: ('ch', chcoords[key]) for key in chcoords})
    if datacoords is not None:
        cube.coords.update({key: (('x', 'y', 'ch'), datacoords[key]) for
            key in datacoords})
    if scalarcoords is not None:
        cube.coords.update(scalarcoords)
    return cube