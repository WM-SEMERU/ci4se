def image_depth(self):
    ifilter = vtk.vtkWindowToImageFilter()
    ifilter.SetInput(self.ren_win)
    ifilter.ReadFrontBufferOff()
    ifilter.SetInputBufferTypeToZBuffer()
    return self._run_image_filter(ifilter)