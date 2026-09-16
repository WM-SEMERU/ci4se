def to_mask(self, method='exact', subpixels=5):
    use_exact, subpixels = self._translate_mask_mode(method, subpixels)
    if hasattr(self, 'a'):
        a = self.a
        b = self.b
    elif hasattr(self, 'a_in'):
        a = self.a_out
        b = self.b_out
        b_in = self.a_in * self.b_out / self.a_out
    else:
        raise ValueError('Cannot determine the aperture shape.')
    masks = []
    for bbox, edges in zip(self.bounding_boxes, self._centered_edges):
        ny, nx = bbox.shape
        mask = elliptical_overlap_grid(edges[0], edges[1], edges[2], edges[
            3], nx, ny, a, b, self.theta, use_exact, subpixels)
        if hasattr(self, 'a_in'):
            mask -= elliptical_overlap_grid(edges[0], edges[1], edges[2],
                edges[3], nx, ny, self.a_in, b_in, self.theta, use_exact,
                subpixels)
        masks.append(ApertureMask(mask, bbox))
    return masks