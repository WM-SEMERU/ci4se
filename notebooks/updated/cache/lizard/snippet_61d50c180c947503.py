def threshold(self, scalars, vmin=None, vmax=None, useCells=False):
    if utils.isSequence(scalars):
        self.addPointScalars(scalars, 'threshold')
        scalars = 'threshold'
    elif self.scalars(scalars) is None:
        colors.printc('~times No scalars found with name', scalars, c=1)
        exit()
    thres = vtk.vtkThreshold()
    thres.SetInputData(self.poly)
    if useCells:
        asso = vtk.vtkDataObject.FIELD_ASSOCIATION_CELLS
    else:
        asso = vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS
    thres.SetInputArrayToProcess(0, 0, 0, asso, scalars)
    if vmin is None and vmax is not None:
        thres.ThresholdByLower(vmax)
    elif vmax is None and vmin is not None:
        thres.ThresholdByUpper(vmin)
    else:
        thres.ThresholdBetween(vmin, vmax)
    thres.Update()
    gf = vtk.vtkGeometryFilter()
    gf.SetInputData(thres.GetOutput())
    gf.Update()
    return self.updateMesh(gf.GetOutput())