def merge_bed_by_name(bt):
    name_lines = dict()
    for r in bt:
        name = r.name
        name_lines[name] = name_lines.get(name, []) + [[r.chrom, r.start, r
            .end, r.name, r.strand]]
    new_lines = []
    for name in name_lines.keys():
        new_lines += _merge_interval_list(name_lines[name])
    new_lines = ['\t'.join(map(str, x)) for x in new_lines]
    return pbt.BedTool('\n'.join(new_lines) + '\n', from_string=True)