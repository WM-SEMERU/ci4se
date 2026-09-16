def _channel(self, width, height, state_sizes, start_level, start_image,
    dataset):
    ret = start_image
    for level, state_size in enumerate(state_sizes, start_level + 1):
        key = dataset + level_dataset(level)
        if start_image is not None:
            scale = self.scanner.level_scale[level - 1]
            width *= scale
            height *= scale
        ret = self.imgtype.create_channel(width, height)
        if start_image is None:
            tr = self.scanner.traversal[0](width, height, ends=False)
            data = self._imgdata(width, height, state_size, '', key)
            self._write_imgdata(ret, data, tr)
        else:
            tr = self.scanner.traversal[0](start_image.size[0], start_image
                .size[1], ends=False)
            for xy in tr:
                start = pixel_to_state(start_image.getpixel(xy))
                data = self._imgdata(scale, scale, state_size, start, key)
                blk = self.scanner.traversal[level](scale, scale, False)
                x, y = xy
                x *= scale
                y *= scale
                self._write_imgdata(ret, data, blk, x, y)
        start_image = ret
    return ret