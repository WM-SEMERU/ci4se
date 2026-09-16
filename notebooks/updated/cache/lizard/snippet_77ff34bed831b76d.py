def get_energy_buckingham(structure, gulp_cmd='gulp', keywords=('optimise',
    'conp', 'qok'), valence_dict=None):
    gio = GulpIO()
    gc = GulpCaller(gulp_cmd)
    gin = gio.buckingham_input(structure, keywords, valence_dict=valence_dict)
    gout = gc.run(gin)
    return gio.get_energy(gout)