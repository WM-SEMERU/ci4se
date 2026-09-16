def set_background(self, image=None, path=None, resize=True):
    if not image and not path:
        raise ValueError(
            'You must either pass a PhotoImage object or a path object')
    if image and path:
        raise ValueError(
            'You must pass either a PhotoImage or str path, not both')
    if image is not None and not isinstance(image, tk.PhotoImage
        ) and not isinstance(image, ImageTk.PhotoImage):
        raise ValueError('The image passed is not a PhotoImage object')
    if path is not None and not isinstance(path, str):
        raise ValueError('The image path passed is not of str type: {0}'.
            format(path))
    if path and not os.path.exists(path):
        raise ValueError('The image path passed is not valid: {0}'.format(path)
            )
    if image is not None:
        self._image = image
    elif path is not None:
        img = Image.open(path)
        if resize:
            img = img.resize((self._canvaswidth, self._canvasheight), Image
                .ANTIALIAS)
        self._image = ImageTk.PhotoImage(img)
    self._background = self.canvas.create_image(0, 0, image=self._image,
        anchor=tk.NW, tag='background')
    self.canvas.tag_lower('background')