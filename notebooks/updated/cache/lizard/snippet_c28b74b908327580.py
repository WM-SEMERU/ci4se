def pon_to_bed(pon_file, out_dir, data):
    out_file = os.path.join(out_dir, '%s-intervals.bed' % utils.
        splitext_plus(os.path.basename(pon_file))[0])
    if not utils.file_uptodate(out_file, pon_file):
        import h5py
        with file_transaction(data, out_file) as tx_out_file:
            with h5py.File(pon_file, 'r') as f:
                with open(tx_out_file, 'w') as out_handle:
                    intervals = f['original_data']['intervals']
                    for i in range(len(intervals[
                        'transposed_index_start_end'][0])):
                        chrom = intervals['indexed_contig_names'][intervals
                            ['transposed_index_start_end'][0][i]]
                        start = int(intervals['transposed_index_start_end']
                            [1][i]) - 1
                        end = int(intervals['transposed_index_start_end'][2][i]
                            )
                        out_handle.write('%s\t%s\t%s\n' % (chrom, start, end))
    return out_file