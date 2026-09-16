def as_artist(self, origin=(0, 0), **kwargs):
    from matplotlib.patches import Ellipse
    xy = self.center.x - origin[0], self.center.y - origin[1]
    width = self.width
    height = self.height
    angle = self.angle.to('deg').value
    mpl_params = self.mpl_properties_default('patch')
    mpl_params.update(kwargs)
    return Ellipse(xy=xy, width=width, height=height, angle=angle, **mpl_params
        )