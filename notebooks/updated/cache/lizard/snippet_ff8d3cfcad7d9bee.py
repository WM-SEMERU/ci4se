def dict_to_vtk(data, path='./dictvtk', voxel_size=1, origin=(0, 0, 0)):
    r
    vs = voxel_size
    for entry in data:
        if data[entry].dtype == bool:
            data[entry] = data[entry].astype(np.int8)
        if data[entry].flags['C_CONTIGUOUS']:
            data[entry] = np.ascontiguousarray(data[entry])
    imageToVTK(path, cellData=data, spacing=(vs, vs, vs), origin=origin)