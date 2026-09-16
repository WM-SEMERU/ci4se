def build_latent_variables(self):
    lvs_to_build = []
    lvs_to_build.append(['Noise Sigma^2', fam.Flat(transform='exp'), fam.
        Normal(0, 3), -1.0])
    for lag in range(self.X.shape[1]):
        lvs_to_build.append(['l lag' + str(lag + 1), fam.FLat(transform=
            'exp'), fam.Normal(0, 3), -1.0])
    lvs_to_build.append(['tau', fam.Flat(transform='exp'), fam.Normal(0, 3),
        -1.0])
    return lvs_to_build