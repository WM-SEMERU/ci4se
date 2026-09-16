def clean_pdb(pdb_file, out_suffix='_clean', outdir=None, force_rerun=False,
    remove_atom_alt=True, keep_atom_alt_id='A', remove_atom_hydrogen=True,
    add_atom_occ=True, remove_res_hetero=True, keep_chemicals=None,
    keep_res_only=None, add_chain_id_if_empty='X', keep_chains=None):
    outfile = ssbio.utils.outfile_maker(inname=pdb_file, append_to_name=
        out_suffix, outdir=outdir, outext='.pdb')
    if ssbio.utils.force_rerun(flag=force_rerun, outfile=outfile):
        my_pdb = StructureIO(pdb_file)
        my_cleaner = CleanPDB(remove_atom_alt=remove_atom_alt,
            remove_atom_hydrogen=remove_atom_hydrogen, keep_atom_alt_id=
            keep_atom_alt_id, add_atom_occ=add_atom_occ, remove_res_hetero=
            remove_res_hetero, keep_res_only=keep_res_only,
            add_chain_id_if_empty=add_chain_id_if_empty, keep_chains=
            keep_chains, keep_chemicals=keep_chemicals)
        my_clean_pdb = my_pdb.write_pdb(out_suffix=out_suffix, out_dir=
            outdir, custom_selection=my_cleaner, force_rerun=force_rerun)
        return my_clean_pdb
    else:
        return outfile