def finalize_vcf(in_file, variantcaller, items):
    out_file = '%s-annotated%s' % utils.splitext_plus(in_file)
    if not utils.file_uptodate(out_file, in_file):
        header_cl = _add_vcf_header_sample_cl(in_file, items, out_file)
        contig_cl = _add_contig_cl(in_file, items, out_file)
        cls = [x for x in (contig_cl, header_cl) if x]
        if cls:
            post_cl = ' | '.join(cls) + ' | '
        else:
            post_cl = None
        dbsnp_file = tz.get_in(('genome_resources', 'variation', 'dbsnp'),
            items[0])
        if dbsnp_file:
            out_file = _add_dbsnp(in_file, dbsnp_file, items[0], out_file,
                post_cl)
    if utils.file_exists(out_file):
        return vcfutils.bgzip_and_index(out_file, items[0]['config'])
    else:
        return in_file