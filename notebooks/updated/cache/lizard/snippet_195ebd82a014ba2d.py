def probePlane(img, origin=(0, 0, 0), normal=(1, 0, 0)):
    plane = vtk.vtkPlane()
    plane.SetOrigin(origin)
    plane.SetNormal(normal)
    planeCut = vtk.vtkCutter()
    planeCut.SetInputData(img)
    planeCut.SetCutFunction(plane)
    planeCut.Update()
    cutActor = Actor(planeCut.GetOutput(), c=None)
    cutActor.mapper.SetScalarRange(img.GetPointData().GetScalars().GetRange())
    return cutActor