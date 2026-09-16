def probePoints(img, pts):
    src = vtk.vtkProgrammableSource()

    def readPoints():
        output = src.GetPolyDataOutput()
        points = vtk.vtkPoints()
        for p in pts:
            x, y, z = p
            points.InsertNextPoint(x, y, z)
        output.SetPoints(points)
        cells = vtk.vtkCellArray()
        cells.InsertNextCell(len(pts))
        for i in range(len(pts)):
            cells.InsertCellPoint(i)
        output.SetVerts(cells)
    src.SetExecuteMethod(readPoints)
    src.Update()
    probeFilter = vtk.vtkProbeFilter()
    probeFilter.SetSourceData(img)
    probeFilter.SetInputConnection(src.GetOutputPort())
    probeFilter.Update()
    pact = Actor(probeFilter.GetOutput(), c=None)
    pact.mapper.SetScalarRange(img.GetScalarRange())
    return pact