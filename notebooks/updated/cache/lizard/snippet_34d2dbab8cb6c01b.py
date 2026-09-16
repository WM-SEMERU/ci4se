def calculate_ideal_atomic_percent(pif):
    if not isinstance(pif, ChemicalSystem):
        return pif
    if not pif.chemical_formula:
        return pif
    else:
        expanded_formula_no_special_char = _expand_formula_(pif.
            chemical_formula)
        element_array = _create_emprical_compositional_array_(
            expanded_formula_no_special_char)
        appended_e_array = _add_atomic_percents_(element_array)
        for e in appended_e_array:
            if _get_element_in_pif_composition_(pif, e['symbol']):
                in_pif = _get_element_in_pif_composition_(pif, e['symbol'])
                comp = in_pif[0]
                pif.composition.pop(in_pif[1])
                comp.idealAtomicPercent = e['atomic_percent']
                pif.composition.append(comp)
            else:
                comp = Composition()
                comp.element = e['symbol']
                comp.idealAtomicPercent = e['atomic_percent']
                pif.composition.append(comp)
        return pif