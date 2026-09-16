def viscosity_kinematic_chem(conc_chem, temp, en_chem):
    if en_chem == 0:
        nu = viscosity_kinematic_alum(conc_chem, temp).magnitude
    if en_chem == 1:
        nu = viscosity_kinematic_pacl(conc_chem, temp).magnitude
    if en_chem not in [0, 1]:
        nu = pc.viscosity_kinematic(temp).magnitude
    return nu