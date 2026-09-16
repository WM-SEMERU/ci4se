def merge_all_models_into_first_model(biop_structure):
    from string import ascii_uppercase
    idx = 1
    first_model = biop_structure[0]
    for m in biop_structure.get_models():
        if first_model.id == m.id:
            continue
        for c in m.get_chains():
            c.id = ascii_uppercase[idx]
            first_model.add(c)
        idx += 1