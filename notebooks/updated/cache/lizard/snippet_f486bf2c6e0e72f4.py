def get_genome_refs(loc_file, loc_type):
    if not file_exists(loc_file):
        return None
    refs = {}
    with open(loc_file) as in_handle:
        for line in in_handle:
            if not line.startswith('#'):
                parts = line.strip().split()
                if loc_type in ['bowtie2', 'samtools', 'alignseq']:
                    refs[parts[1]] = parts[-1]
                else:
                    refs[parts[0]] = parts[-1]
    return refs