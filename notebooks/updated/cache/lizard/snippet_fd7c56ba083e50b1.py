def perimeter(self):
    if self._is_completely_masked:
        return np.nan * u.pix
    else:
        from skimage.measure import perimeter
        return perimeter(~self._total_mask, neighbourhood=4) * u.pix