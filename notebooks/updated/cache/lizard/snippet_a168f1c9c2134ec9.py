def create_single_structure_pse(structure_name, structure_content,
    residue_ids_of_interest, pymol_executable='pymol', settings={}):
    b = BatchBuilder(pymol_executable=pymol_executable)
    PSE_files = b.run(SingleStructureBuilder, [{structure_name:
        PDBContainer(structure_name, structure_content,
        residue_ids_of_interest)}], settings=settings)
    return PSE_files[0], b.PSE_scripts[0]