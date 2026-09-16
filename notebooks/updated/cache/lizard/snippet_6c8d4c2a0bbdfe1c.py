def _split_by_regions(dirname, out_ext, in_key):

    def _do_work(data):
        regions = _get_parallel_regions(data)

        def _sort_by_size(region):
            _, start, end = region
            return end - start
        regions.sort(key=_sort_by_size, reverse=True)
        bam_file = data[in_key]
        if bam_file is None:
            return None, []
        part_info = []
        base_out = os.path.splitext(os.path.basename(bam_file))[0]
        nowork = [['nochrom'], ['noanalysis', data['config']['algorithm'][
            'non_callable_regions']]]
        for region in (regions + nowork):
            out_dir = os.path.join(data['dirs']['work'], dirname, data[
                'name'][-1], region[0])
            region_outfile = os.path.join(out_dir, '%s-%s%s' % (base_out,
                to_safestr(region), out_ext))
            part_info.append((region, region_outfile))
        out_file = os.path.join(data['dirs']['work'], dirname, data['name']
            [-1], '%s%s' % (base_out, out_ext))
        return out_file, part_info
    return _do_work