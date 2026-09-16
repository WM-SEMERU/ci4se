def create_color(color):
    if color[0] == '#':
        return [(int(color[i:i + 2], 16) / 255) for i in range(1, 7, 2)]
    else:
        nc = vtk.vtkNamedColors()
        return nc.GetColor3d(color)