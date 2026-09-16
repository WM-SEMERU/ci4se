def outline_corners(dataset, factor=0.2):
    alg = vtk.vtkOutlineCornerFilter()
    alg.SetInputDataObject(dataset)
    alg.SetCornerFactor(factor)
    alg.Update()
    return wrap(alg.GetOutputDataObject(0))