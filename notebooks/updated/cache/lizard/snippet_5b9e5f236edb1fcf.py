def image(self, render_mode):
    if render_mode == RenderMode.COLOR:
        return self.color_im
    elif render_mode == RenderMode.DEPTH:
        return self.depth_im
    elif render_mode == RenderMode.SEGMASK:
        return self.binary_im
    else:
        return None