def mask_binary(self, binary_im):
    color = self.color.mask_binary(binary_im)
    depth = self.depth.mask_binary(binary_im)
    return RgbdImage.from_color_and_depth(color, depth)