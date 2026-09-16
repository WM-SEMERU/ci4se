def submit_vasp_directory(self, rootdir, authors, projects=None, references
    ='', remarks=None, master_data=None, master_history=None, created_at=
    None, ncpus=None):
    from pymatgen.apps.borg.hive import VaspToComputedEntryDrone
    from pymatgen.apps.borg.queen import BorgQueen
    drone = VaspToComputedEntryDrone(inc_structure=True, data=['filename',
        'initial_structure'])
    queen = BorgQueen(drone, number_of_drones=ncpus)
    queen.parallel_assimilate(rootdir)
    structures = []
    metadata = []
    histories = []
    for e in queen.get_data():
        structures.append(e.structure)
        m = {'_vasp': {'parameters': e.parameters, 'final_energy': e.energy,
            'final_energy_per_atom': e.energy_per_atom, 'initial_structure':
            e.data['initial_structure'].as_dict()}}
        if 'history' in e.parameters:
            histories.append(e.parameters['history'])
        if master_data is not None:
            m.update(master_data)
        metadata.append(m)
    if master_history is not None:
        histories = master_history * len(structures)
    return self.submit_structures(structures, authors, projects=projects,
        references=references, remarks=remarks, data=metadata, histories=
        histories, created_at=created_at)