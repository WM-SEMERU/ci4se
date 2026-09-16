def rotate_to_zaxis(self, new_zaxis):
    img = self._rotate_end(self.img, self.zaxis)
    seeds = self._rotate_end(self.seeds, self.zaxis)
    contour = self._rotate_end(self.contour, self.zaxis)
    self.img = self._rotate_start(img, new_zaxis)
    self.seeds = self._rotate_start(seeds, new_zaxis)
    self.contour = self._rotate_start(contour, new_zaxis)
    self.zaxis = new_zaxis
    self.actual_slice = 0
    self.rotated_back = False
    self.fig.delaxes(self.ax_actual_slice)
    self.ax_actual_slice.cla()
    del self.actual_slice_slider
    self.fig.add_axes(self.ax_actual_slice)
    self.actual_slice_slider = Slider(self.ax_actual_slice, 'Slice', 0, 
        self.img.shape[2] - 1, valinit=0)
    self.actual_slice_slider.on_changed(self.sliceslider_update)
    self.update_slice()