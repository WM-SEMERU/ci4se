def _calc_rms(mol1, mol2, clabel1, clabel2):
    obmol1 = BabelMolAdaptor(mol1).openbabel_mol
    obmol2 = BabelMolAdaptor(mol2).openbabel_mol
    cmol1 = ob.OBMol()
    for i in clabel1:
        oa1 = obmol1.GetAtom(i)
        a1 = cmol1.NewAtom()
        a1.SetAtomicNum(oa1.GetAtomicNum())
        a1.SetVector(oa1.GetVector())
    cmol2 = ob.OBMol()
    for i in clabel2:
        oa2 = obmol2.GetAtom(i)
        a2 = cmol2.NewAtom()
        a2.SetAtomicNum(oa2.GetAtomicNum())
        a2.SetVector(oa2.GetVector())
    aligner = ob.OBAlign(True, False)
    aligner.SetRefMol(cmol1)
    aligner.SetTargetMol(cmol2)
    aligner.Align()
    return aligner.GetRMSD()