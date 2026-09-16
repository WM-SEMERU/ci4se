def from_poscar_string(poscar_string, transformations=None):
    p = Poscar.from_string(poscar_string)
    if not p.true_names:
        raise ValueError(
            'Transformation can be craeted only from POSCAR strings with proper VASP5 element symbols.'
            )
    raw_string = re.sub("'", '"', poscar_string)
    s = p.structure
    source_info = {'source': 'POSCAR', 'datetime': str(datetime.datetime.
        now()), 'original_file': raw_string}
    return TransformedStructure(s, transformations, history=[source_info])