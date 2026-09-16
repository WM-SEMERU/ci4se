def makeMet(segID, N, CA, C, O, geo):
    CA_CB_length = geo.CA_CB_length
    C_CA_CB_angle = geo.C_CA_CB_angle
    N_C_CA_CB_diangle = geo.N_C_CA_CB_diangle
    CB_CG_length = geo.CB_CG_length
    CA_CB_CG_angle = geo.CA_CB_CG_angle
    N_CA_CB_CG_diangle = geo.N_CA_CB_CG_diangle
    CG_SD_length = geo.CG_SD_length
    CB_CG_SD_angle = geo.CB_CG_SD_angle
    CA_CB_CG_SD_diangle = geo.CA_CB_CG_SD_diangle
    SD_CE_length = geo.SD_CE_length
    CG_SD_CE_angle = geo.CG_SD_CE_angle
    CB_CG_SD_CE_diangle = geo.CB_CG_SD_CE_diangle
    carbon_b = calculateCoordinates(N, C, CA, CA_CB_length, C_CA_CB_angle,
        N_C_CA_CB_diangle)
    CB = Atom('CB', carbon_b, 0.0, 1.0, ' ', ' CB', 0, 'C')
    carbon_g = calculateCoordinates(N, CA, CB, CB_CG_length, CA_CB_CG_angle,
        N_CA_CB_CG_diangle)
    CG = Atom('CG', carbon_g, 0.0, 1.0, ' ', ' CG', 0, 'C')
    sulfur_d = calculateCoordinates(CA, CB, CG, CG_SD_length,
        CB_CG_SD_angle, CA_CB_CG_SD_diangle)
    SD = Atom('SD', sulfur_d, 0.0, 1.0, ' ', ' SD', 0, 'S')
    carbon_e = calculateCoordinates(CB, CG, SD, SD_CE_length,
        CG_SD_CE_angle, CB_CG_SD_CE_diangle)
    CE = Atom('CE', carbon_e, 0.0, 1.0, ' ', ' CE', 0, 'C')
    res = Residue((' ', segID, ' '), 'MET', '    ')
    res.add(N)
    res.add(CA)
    res.add(C)
    res.add(O)
    res.add(CB)
    res.add(CG)
    res.add(SD)
    res.add(CE)
    return res