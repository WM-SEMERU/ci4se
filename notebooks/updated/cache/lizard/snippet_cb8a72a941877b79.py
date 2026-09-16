def color_by_height(self, axis=1, threshold=None, color=DEFAULT_COLORMAP):
    import numpy as np
    heights = self.v[:, (axis)] - self.floor_point[axis]
    if threshold:
        color_weights = np.minimum(heights / threshold, 1.0)
        color_weights = color_weights * color_weights
        self.set_vertex_colors_from_weights(color_weights, scale_to_range_1
            =False)
    else:
        self.set_vertex_colors_from_weights(heights)