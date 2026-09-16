def set_image(self, image, add_to_canvas=True):
    if not isinstance(image, BaseImage.BaseImage):
        raise ValueError('Wrong type of object to load: %s' % str(type(image)))
    canvas_img = self.get_canvas_image()
    old_image = canvas_img.get_image()
    self.make_callback('image-unset', old_image)
    with self.suppress_redraw:
        canvas_img.set_image(image)
        if add_to_canvas:
            try:
                self.canvas.get_object_by_tag(self._canvas_img_tag)
            except KeyError:
                self.canvas.add(canvas_img, tag=self._canvas_img_tag)
            self.canvas.lower_object(canvas_img)