def _sanitize_input_structure(input_structure):
    input_structure = input_structure.copy()
    input_structure.remove_spin()
    input_structure = input_structure.get_primitive_structure(use_site_props
        =False)
    if 'magmom' in input_structure.site_properties:
        input_structure.remove_site_property('magmom')
    return input_structure