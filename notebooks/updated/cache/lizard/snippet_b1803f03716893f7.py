def get_splicejunction_file(align_dir, data):
    samplename = dd.get_sample_name(data)
    align_dir = os.path.dirname(dd.get_work_bam(data))
    knownfile = get_known_splicesites_file(align_dir, data)
    novelfile = os.path.join(align_dir, '%s-novelsplicesites.bed' % samplename)
    bed_files = [x for x in [knownfile, novelfile] if file_exists(x)]
    splicejunction = bed.concat(bed_files)
    splicejunctionfile = os.path.join(align_dir, '%s-splicejunctions.bed' %
        samplename)
    if splicejunction:
        splicejunction.saveas(splicejunctionfile)
        return splicejunctionfile
    else:
        return None