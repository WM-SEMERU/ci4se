def filter_junction_variants(vrn_file, data):
    SJ_BP_MASK = 10
    vrn_dir = os.path.dirname(vrn_file)
    splicebed = dd.get_junction_bed(data)
    if not file_exists(splicebed):
        logger.info(
            'Splice junction BED file not found, skipping filtering of variants closed to splice junctions.'
            )
        return vrn_file
    spliceslop = get_padded_bed_file(vrn_dir, splicebed, SJ_BP_MASK, data)
    out_file = os.path.splitext(vrn_file)[0] + '-junctionfiltered.vcf.gz'
    if file_exists(out_file):
        return out_file
    with file_transaction(data, out_file) as tx_out_file:
        out_base = os.path.splitext(tx_out_file)[0]
        logger.info(
            'Removing variants within %d bases of splice junctions listed in %s from %s. '
             % (SJ_BP_MASK, spliceslop, vrn_file))
        pybedtools.BedTool(vrn_file).intersect(spliceslop, wa=True, header=
            True, v=True).saveas(out_base)
        tx_out_file = vcfutils.bgzip_and_index(out_base, dd.get_config(data))
    return out_file