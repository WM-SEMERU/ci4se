def write_pdb(self, custom_name='', out_suffix='', out_dir=None,
    custom_selection=None, force_rerun=False):
    if not custom_selection:
        custom_selection = ModelSelection([0])
    if not out_dir or not custom_name:
        if not out_suffix:
            out_suffix = '_new'
    outfile = ssbio.utils.outfile_maker(inname=self.structure_file, outname
        =custom_name, append_to_name=out_suffix, outdir=out_dir, outext='.pdb')
    try:
        if ssbio.utils.force_rerun(flag=force_rerun, outfile=outfile):
            self.save(outfile, custom_selection)
    except TypeError as e:
        log.error('{}: unable to save structure in PDB file format'.format(
            self.structure_file))
        raise TypeError(e)
    return outfile