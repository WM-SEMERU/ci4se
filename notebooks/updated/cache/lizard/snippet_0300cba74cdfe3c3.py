def add_leverage(self):
    if self.leverage is True:
        pass
    else:
        self.leverage = True
        self.z_no += 1
        self.latent_variables.z_list.pop()
        self.latent_variables.z_list.pop()
        self.latent_variables.z_list.pop()
        self.latent_variables.z_list.pop()
        self.latent_variables.add_z('Leverage Term', fam.Flat(transform=
            None), fam.Normal(0, 3))
        self.latent_variables.add_z('Skewness', fam.Flat(transform='exp'),
            fam.Normal(0, 3))
        self.latent_variables.add_z('v', fam.Flat(transform='exp'), fam.
            Normal(0, 3))
        self.latent_variables.add_z('Returns Constant', fam.Normal(0, 3,
            transform=None), fam.Normal(0, 3))
        self.latent_variables.add_z('GARCH-M', fam.Normal(0, 3, transform=
            None), fam.Normal(0, 3))
        self.latent_variables.z_list[-3].start = 2.0