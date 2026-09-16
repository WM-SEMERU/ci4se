def filter_for_ligands(self):
    candidates1 = [o for o in pybel.ob.OBResidueIter(self.proteincomplex.
        OBMol) if not o.GetResidueProperty(9) and self.is_het_residue(o)]
    if config.DNARECEPTOR:
        candidates1 = [res for res in candidates1 if res.GetName() not in 
            config.DNA + config.RNA]
    all_lignames = set([a.GetName() for a in candidates1])
    water = [o for o in pybel.ob.OBResidueIter(self.proteincomplex.OBMol) if
        o.GetResidueProperty(9)]
    if not config.KEEPMOD:
        candidates2 = [a for a in candidates1 if is_lig(a.GetName()) and a.
            GetName() not in self.modresidues]
    else:
        candidates2 = [a for a in candidates1 if is_lig(a.GetName())]
    write_message('%i ligand(s) after first filtering step.\n' % len(
        candidates2), mtype='debug')
    artifacts = []
    unique_ligs = set(a.GetName() for a in candidates2)
    for ulig in unique_ligs:
        if ulig in config.biolip_list and [a.GetName() for a in candidates2
            ].count(ulig) >= 15:
            artifacts.append(ulig)
    selected_ligands = [a for a in candidates2 if a.GetName() not in artifacts]
    return selected_ligands, all_lignames, water