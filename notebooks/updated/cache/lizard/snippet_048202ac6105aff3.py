def get_reference_genome_file(refseqdir, build):
    if not os.path.exists(refseqdir) or not os.path.isdir(refseqdir):
        raise ValueError('No directory at {}'.format(refseqdir))
    twobit_name = ''
    if build in ['b37', 'build 37', 'build37', '37', 'hg19']:
        twobit_name = 'hg19.2bit'
        build = 'build37'
    if not twobit_name:
        raise ValueError('Genome bulid "{}" not supported.'.format(build))
    twobit_path = os.path.join(refseqdir, twobit_name)
    if not os.path.exists(twobit_path):
        twobitdownload.save_genome('hg19', destdir=refseqdir)
    return twobit_path, twobit_name