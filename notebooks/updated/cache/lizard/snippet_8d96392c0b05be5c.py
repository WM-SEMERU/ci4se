def select(self):
    if self.GUI == None:
        return
    self.GUI.current_fit = self
    if self.tmax != None and self.tmin != None:
        self.GUI.update_bounds_boxes()
    if self.PCA_type != None:
        self.GUI.update_PCA_box()
    try:
        self.GUI.zijplot
    except AttributeError:
        self.GUI.draw_figure(self.GUI.s)
    self.GUI.fit_box.SetStringSelection(self.name)
    self.GUI.get_new_PCA_parameters(-1)