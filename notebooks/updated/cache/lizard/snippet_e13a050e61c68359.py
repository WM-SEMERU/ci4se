def get_protein_feather_paths(protgroup, memornot, protgroup_dict,
    protein_feathers_dir, core_only_genes=None):
    prots_memornot = protgroup_dict['localization'][memornot[0]][memornot[1]]
    if protgroup[0] == 'localization':
        if protgroup[2] != 'all':
            if memornot[1] in ['membrane', 'inner_membrane', 'outer_membrane'
                ] and protgroup[2] not in ['membrane', 'inner_membrane',
                'outer_membrane']:
                return []
            if memornot[1] not in ['membrane', 'inner_membrane',
                'outer_membrane'] and protgroup[2] in ['membrane',
                'inner_membrane', 'outer_membrane']:
                return []
    prots_group = protgroup_dict[protgroup[0]][protgroup[1]][protgroup[2]]
    prots_filtered = list(set(prots_group).intersection(prots_memornot))
    if core_only_genes:
        prots_filtered = list(set(prots_filtered).intersection(core_only_genes)
            )
    return [op.join(protein_feathers_dir,
        '{}_protein_strain_properties.fthr'.format(x)) for x in
        prots_filtered if op.exists(op.join(protein_feathers_dir,
        '{}_protein_strain_properties.fthr'.format(x)))]