def get_pan(self, coord='data'):
    pan_x, pan_y = self.t_['pan'][:2]
    if coord == 'wcs':
        if self.t_['pan_coord'] == 'data':
            image = self.get_image()
            if image is not None:
                try:
                    return image.pixtoradec(pan_x, pan_y)
                except Exception as e:
                    pass
        return pan_x, pan_y
    if self.t_['pan_coord'] == 'data':
        return pan_x, pan_y
    image = self.get_image()
    if image is not None:
        try:
            return image.radectopix(pan_x, pan_y)
        except Exception as e:
            pass
    return pan_x, pan_y