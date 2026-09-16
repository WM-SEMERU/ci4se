def __update(self):
    width, height = self.size
    super(BaseWidget, self).__setattr__('width', width)
    super(BaseWidget, self).__setattr__('height', height)
    super(BaseWidget, self).__setattr__(self.anchor, self.pos)