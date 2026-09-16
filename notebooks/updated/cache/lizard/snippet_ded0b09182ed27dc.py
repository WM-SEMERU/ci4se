def get_par_group_contribution(self, include_prior_results=False):
    pargrp_dict = {}
    par = self.pst.parameter_data
    groups = par.groupby('pargp').groups
    for grp, idxs in groups.items():
        pargrp_dict[grp] = [pname for pname in list(par.loc[idxs, 'parnme']
            ) if pname in self.jco.col_names and pname in self.parcov.row_names
            ]
    return self.get_par_contribution(pargrp_dict, include_prior_results=
        include_prior_results)