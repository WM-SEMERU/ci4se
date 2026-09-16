def read_pybel(value, name=None):
    if isinstance(value, _pb.Molecule):
        jobfilename = None
        charge, mult = value.charge, value.spin
        ccdata = _makecclib(value.OBMol)
    elif isinstance(value, _ob.OBMol):
        jobfilename = None
        charge, mult = value.GetTotalCharge(), value.GetTotalSpinMultiplicity()
        ccdata = _makecclib(value)
    else:
        jobfilename = value
        _, jobfilename_ext = _os.path.splitext(jobfilename)
        mol = next(_pb.readfile(jobfilename_ext[1:], jobfilename))
        charge, mult = mol.charge, mol.spin
        ccdata = _makecclib(mol.OBMol)
    if name is None:
        name = jobfilename
    attributes = ccdata.getattributes()
    attributes.update({'name': name, 'jobfilename': jobfilename, 'charge':
        charge, 'mult': mult})
    return Atoms(attributes)