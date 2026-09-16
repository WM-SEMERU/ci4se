def build_increments(self):
    self.enforce_bounds()
    self.add_transform_columns()
    par_groups = self.parameter_data.groupby('pargp').groups
    inctype = self.parameter_groups.groupby('inctyp').groups
    for itype, inc_groups in inctype.items():
        pnames = []
        for group in inc_groups:
            pnames.extend(par_groups[group])
            derinc = self.parameter_groups.loc[group, 'derinc']
            self.parameter_data.loc[par_groups[group], 'derinc'] = derinc
        if itype == 'absolute':
            self.parameter_data.loc[pnames, 'increment'
                ] = self.parameter_data.loc[pnames, 'derinc']
        elif itype == 'relative':
            self.parameter_data.loc[pnames, 'increment'
                ] = self.parameter_data.loc[pnames, 'derinc'
                ] * self.parameter_data.loc[pnames, 'parval1']
        elif itype == 'rel_to_max':
            mx = self.parameter_data.loc[pnames, 'parval1'].max()
            self.parameter_data.loc[pnames, 'increment'
                ] = self.parameter_data.loc[pnames, 'derinc'] * mx
        else:
            raise Exception('Pst.get_derivative_increments(): ' +
                'unrecognized increment type:{0}'.format(itype))
    isfixed = self.parameter_data.partrans == 'fixed'
    self.parameter_data.loc[isfixed, 'increment'] = self.parameter_data.loc[
        isfixed, 'parval1']