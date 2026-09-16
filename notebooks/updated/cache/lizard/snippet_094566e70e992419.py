def write_gff_file(self, outfile, force_rerun=False):
    if ssbio.utils.force_rerun(outfile=outfile, flag=force_rerun):
        with open(outfile, 'w') as out_handle:
            GFF.write([self], out_handle)
    self.feature_path = outfile