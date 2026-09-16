def write_input(self, output_dir='.', make_dir_if_not_present=True):
    if make_dir_if_not_present and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    feff = self.all_input()
    feff_input = '\n\n'.join(str(feff[k]) for k in ['HEADER', 'PARAMETERS',
        'POTENTIALS', 'ATOMS'] if k in feff)
    for k, v in feff.items():
        with open(os.path.join(output_dir, k), 'w') as f:
            f.write(str(v))
    with open(os.path.join(output_dir, 'feff.inp'), 'w') as f:
        f.write(feff_input)
    if 'ATOMS' not in feff:
        self.atoms.struct.to(fmt='cif', filename=os.path.join(output_dir,
            feff['PARAMETERS']['CIF']))