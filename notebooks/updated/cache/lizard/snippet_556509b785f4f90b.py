def convexHull(actor_or_list, alphaConstant=0):
    if vu.isSequence(actor_or_list):
        actor = vs.Points(actor_or_list)
    else:
        actor = actor_or_list
    apoly = actor.clean().polydata()
    triangleFilter = vtk.vtkTriangleFilter()
    triangleFilter.SetInputData(apoly)
    triangleFilter.Update()
    poly = triangleFilter.GetOutput()
    delaunay = vtk.vtkDelaunay3D()
    if alphaConstant:
        delaunay.SetAlpha(alphaConstant)
    delaunay.SetInputData(poly)
    delaunay.Update()
    surfaceFilter = vtk.vtkDataSetSurfaceFilter()
    surfaceFilter.SetInputConnection(delaunay.GetOutputPort())
    surfaceFilter.Update()
    chuact = Actor(surfaceFilter.GetOutput())
    return chuact