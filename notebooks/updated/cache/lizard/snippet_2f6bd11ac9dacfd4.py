def to_sdf(self):
    skel, sdf_in = morph.medial_axis(self.data, return_distance=True)
    useless_skel, sdf_out = morph.medial_axis(np.iinfo(np.uint8).max - self
        .data, return_distance=True)
    sdf = sdf_out - sdf_in
    return sdf