def display(self, cutout, use_pixel_coords=False):
    logging.debug('Current display list contains: {}'.format(self.
        _displayables_by_cutout.keys()))
    logging.debug('Looking for {}'.format(cutout))
    assert isinstance(cutout, SourceCutout)
    if cutout in self._displayables_by_cutout:
        displayable = self._displayables_by_cutout[cutout]
    else:
        displayable = self._create_displayable(cutout)
        self._displayables_by_cutout[cutout] = displayable
    self._detach_handlers(self.current_displayable)
    self.current_cutout = cutout
    self.current_displayable = displayable
    self._attach_handlers(self.current_displayable)
    self._do_render(self.current_displayable)
    self.mark_apertures(cutout, pixel=use_pixel_coords)
    self.draw_uncertainty_ellipse(cutout)