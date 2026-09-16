def _remove_prioritization(in_file, data, out_dir=None):
    out_file = '%s-germline.vcf' % utils.splitext_plus(in_file)[0]
    if out_dir:
        out_file = os.path.join(out_dir, os.path.basename(out_file))
    if not utils.file_uptodate(out_file, in_file) and not utils.file_uptodate(
        out_file + '.gz', in_file):
        with file_transaction(data, out_file) as tx_out_file:
            reader = cyvcf2.VCF(str(in_file))
            reader.add_filter_to_header({'ID': 'Somatic', 'Description':
                'Variant called as Somatic'})
            with contextlib.closing(cyvcf2.Writer(tx_out_file, reader)
                ) as writer:
                for rec in reader:
                    rec = _update_prioritization_filters(rec)
                    writer.write_record(rec)
    return out_file