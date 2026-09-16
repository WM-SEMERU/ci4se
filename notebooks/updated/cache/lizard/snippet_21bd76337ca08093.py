def contains_vasp_input(dir_name):
    for f in ['INCAR', 'POSCAR', 'POTCAR', 'KPOINTS']:
        if not os.path.exists(os.path.join(dir_name, f)
            ) and not os.path.exists(os.path.join(dir_name, f + '.orig')):
            return False
    return True