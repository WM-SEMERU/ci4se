def makeVal(segID, N, CA, C, O, geo):
    CA_CB_length = geo.CA_CB_length
    C_CA_CB_angle = geo.C_CA_CB_angle
    N_C_CA_CB_diangle = geo.N_C_CA_CB_diangle
    CB_CG1_length = geo.CB_CG1_length
    CA_CB_CG1_angle = geo.CA_CB_CG1_angle
    N_CA_CB_CG1_diangle = geo.N_CA_CB_CG1_diangle
    CB_CG2_length = geo.CB_CG2_length
    CA_CB_CG2_angle = geo.CA_CB_CG2_angle
    N_CA_CB_CG2_diangle = geo.N_CA_CB_CG2_diangle
    carbon_b = calculateCoordinates(N, C, CA, CA_CB_length, C_CA_CB_angle,
        N_C_CA_CB_diangle)
    CB = Atom('CB', carbon_b, 0.0, 1.0, ' ', ' CB', 0, 'C')
    carbon_g1 = calculateCoordinates(N, CA, CB, CB_CG1_length,
        CA_CB_CG1_angle, N_CA_CB_CG1_diangle)
    CG1 = Atom('CG1', carbon_g1, 0.0, 1.0, ' ', ' CG1', 0, 'C')
    carbon_g2 = calculateCoordinates(N, CA, CB, CB_CG2_length,
        CA_CB_CG2_angle, N_CA_CB_CG2_diangle)
    CG2 = Atom('CG2', carbon_g2, 0.0, 1.0, ' ', ' CG2', 0, 'C')
    res = Residue((' ', segID, ' '), 'VAL', '    ')
    res.add(N)
    res.add(CA)
    res.add(C)
    res.add(O)
    res.add(CB)
    res.add(CG1)
    res.add(CG2)
    return res