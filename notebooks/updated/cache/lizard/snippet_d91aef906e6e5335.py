def cutWithPlane(self, origin=(0, 0, 0), normal=(1, 0, 0), showcut=False):
    if normal is 'x':
        normal = 1, 0, 0
    elif normal is 'y':
        normal = 0, 1, 0
    elif normal is 'z':
        normal = 0, 0, 1
    plane = vtk.vtkPlane()
    plane.SetOrigin(origin)
    plane.SetNormal(normal)
    self.computeNormals()
    poly = self.polydata()
    clipper = vtk.vtkClipPolyData()
    clipper.SetInputData(poly)
    clipper.SetClipFunction(plane)
    if showcut:
        clipper.GenerateClippedOutputOn()
    else:
        clipper.GenerateClippedOutputOff()
    clipper.GenerateClipScalarsOff()
    clipper.SetValue(0)
    clipper.Update()
    self.updateMesh(clipper.GetOutput())
    if showcut:
        c = self.GetProperty().GetColor()
        cpoly = clipper.GetClippedOutput()
        restActor = Actor(cpoly, c=c, alpha=0.05, wire=1)
        restActor.SetUserMatrix(self.GetMatrix())
        asse = Assembly([self, restActor])
        self = asse
        return asse
    else:
        return self