def _subset_by_support(orig_vcf, cmp_calls, data):
    cmp_vcfs = [x['vrn_file'] for x in cmp_calls]
    out_file = '%s-inensemble.vcf.gz' % utils.splitext_plus(orig_vcf)[0]
    if not utils.file_uptodate(out_file, orig_vcf):
        with file_transaction(data, out_file) as tx_out_file:
            cmd = 'bedtools intersect -header -wa -f 0.5 -r -a {orig_vcf} -b '
            for cmp_vcf in cmp_vcfs:
                cmd += "<(bcftools view -f 'PASS,.' %s) " % cmp_vcf
            cmd += '| bgzip -c > {tx_out_file}'
            do.run(cmd.format(**locals()),
                'Subset calls by those present in Ensemble output')
    return vcfutils.bgzip_and_index(out_file, data['config'])