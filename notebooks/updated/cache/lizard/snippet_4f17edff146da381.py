def set_auxiliary_basis_set(self, folder, auxiliary_folder,
    auxiliary_basis_set_type='aug_cc_pvtz'):
    list_files = os.listdir(auxiliary_folder)
    for specie in self._mol.symbol_set:
        for file in list_files:
            if file.upper().find(specie.upper() + '2') != -1 and file.lower(
                ).find(auxiliary_basis_set_type) != -1:
                shutil.copyfile(auxiliary_folder + '/' + file, folder + '/' +
                    specie + '2.ion')