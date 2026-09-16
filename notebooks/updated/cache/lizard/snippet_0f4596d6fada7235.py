def minimize(bed_file):
    if not bed_file:
        return bed_file
    else:
        sorted_bed = bt.BedTool(bed_file).cut(range(3)).sort()
        if not sorted_bed.fn.endswith('.bed'):
            return sorted_bed.moveto(sorted_bed.fn + '.bed')
        else:
            return sorted_bed