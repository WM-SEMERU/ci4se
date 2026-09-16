def add_triangle(self, neighbors, color, center=None, opacity=0.4,
    draw_edges=False, edges_color=[0.0, 0.0, 0.0], edges_linewidth=2):
    points = vtk.vtkPoints()
    triangle = vtk.vtkTriangle()
    for ii in range(3):
        points.InsertNextPoint(neighbors[ii].x, neighbors[ii].y, neighbors[
            ii].z)
        triangle.GetPointIds().SetId(ii, ii)
    triangles = vtk.vtkCellArray()
    triangles.InsertNextCell(triangle)
    trianglePolyData = vtk.vtkPolyData()
    trianglePolyData.SetPoints(points)
    trianglePolyData.SetPolys(triangles)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInput(trianglePolyData)
    ac = vtk.vtkActor()
    ac.SetMapper(mapper)
    ac.GetProperty().SetOpacity(opacity)
    if color == 'element':
        if center is None:
            raise ValueError(
                'Color should be chosen according to the central atom, and central atom is not provided'
                )
        myoccu = 0.0
        for specie, occu in center.species.items():
            if occu > myoccu:
                myspecie = specie
                myoccu = occu
        color = [(i / 255) for i in self.el_color_mapping[myspecie.symbol]]
        ac.GetProperty().SetColor(color)
    else:
        ac.GetProperty().SetColor(color)
    if draw_edges:
        ac.GetProperty().SetEdgeColor(edges_color)
        ac.GetProperty().SetLineWidth(edges_linewidth)
        ac.GetProperty().EdgeVisibilityOn()
    self.ren.AddActor(ac)