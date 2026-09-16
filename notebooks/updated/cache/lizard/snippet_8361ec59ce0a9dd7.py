def from_polymers(cls, polymers):
    n = len(polymers)
    instance = cls(n=n, auto_build=False)
    instance.major_radii = [x.major_radius for x in polymers]
    instance.major_pitches = [x.major_pitch for x in polymers]
    instance.major_handedness = [x.major_handedness for x in polymers]
    instance.aas = [x.num_monomers for x in polymers]
    instance.minor_helix_types = [x.minor_helix_type for x in polymers]
    instance.orientations = [x.orientation for x in polymers]
    instance.phi_c_alphas = [x.phi_c_alpha for x in polymers]
    instance.minor_repeats = [x.minor_repeat for x in polymers]
    instance.build()
    return instance