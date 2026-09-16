def frames(self, skip_registration=False):
    color_im, depth_im, ir_im, _ = self._frames_and_index_map(skip_registration
        =skip_registration)
    return color_im, depth_im, ir_im