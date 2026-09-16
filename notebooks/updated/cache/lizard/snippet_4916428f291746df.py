def convex_hull(self):
    hull_array = skimage.morphology.convex_hull_image(self.bitmap)
    return Region(hull_array)