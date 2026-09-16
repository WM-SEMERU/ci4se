def rstrip_extra(fname):
    to_strip = '_R', '.R', '-R', '_', 'fastq', '.', '-'
    while fname.endswith(to_strip):
        for x in to_strip:
            if fname.endswith(x):
                fname = fname[:len(fname) - len(x)]
                break
    return fname