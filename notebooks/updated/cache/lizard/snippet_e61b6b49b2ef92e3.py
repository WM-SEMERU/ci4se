def loadfn(fname):
    if (fnmatch(fname, '*POSCAR*') or fnmatch(fname, '*CONTCAR*') or '.cif' in
        fname.lower()) or fnmatch(fname, '*.vasp'):
        return Structure.from_file(fname)
    elif fnmatch(fname, '*vasprun*'):
        from pymatgen.io.vasp import Vasprun
        return Vasprun(fname)
    elif fnmatch(fname, '*.json*'):
        from monty.serialization import loadfn
        return loadfn(fname)