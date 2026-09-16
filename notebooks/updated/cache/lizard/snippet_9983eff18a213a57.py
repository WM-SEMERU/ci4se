def _create_pileup(bam_file, data, out_base, background):
    out_file = '%s-mpileup.txt' % out_base
    if not utils.file_exists(out_file):
        with file_transaction(data, out_file) as tx_out_file:
            background_bed = os.path.normpath(os.path.join(os.path.dirname(
                os.path.realpath(utils.which('verifybamid2'))), 'resource',
                '%s.%s.%s.vcf.gz.dat.bed' % (background['dataset'],
                background['nvars'], background['build'])))
            local_bed = os.path.join(os.path.dirname(out_base), 
                '%s.%s-hg19.bed' % (background['dataset'], background['nvars'])
                )
            if not utils.file_exists(local_bed):
                with file_transaction(data, local_bed) as tx_local_bed:
                    with open(background_bed) as in_handle:
                        with open(tx_local_bed, 'w') as out_handle:
                            for line in in_handle:
                                out_handle.write('chr%s' % line)
            mpileup_cl = samtools.prep_mpileup([bam_file], dd.get_ref_file(
                data), data['config'], want_bcf=False, target_regions=local_bed
                )
            cl = "{mpileup_cl} | sed 's/^chr//' > {tx_out_file}"
            do.run(cl.format(**locals()), 'Create pileup from BAM input')
    return out_file