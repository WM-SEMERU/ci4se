def left_button_down(self, obj, event_type):
    click_pos = self.iren.GetEventPosition()
    picker = vtk.vtkWorldPointPicker()
    picker.Pick(click_pos[0], click_pos[1], 0, self.renderer)
    self.pickpoint = np.asarray(picker.GetPickPosition()).reshape((-1, 3))
    if np.any(np.isnan(self.pickpoint)):
        self.pickpoint[:] = 0