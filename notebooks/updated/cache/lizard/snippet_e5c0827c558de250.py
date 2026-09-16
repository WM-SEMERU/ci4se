def contrast(self, color, step):
    hls = colorsys.rgb_to_hls(*self.rgb(color))
    if self.is_light(color):
        return colorsys.hls_to_rgb(hls[0], hls[1] - step, hls[2])
    else:
        return colorsys.hls_to_rgb(hls[0], hls[1] + step, hls[2])