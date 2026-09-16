def _can_use_mem(fastq_file, data, read_min_size=None):
    min_size = 70
    if read_min_size and read_min_size >= min_size:
        return True
    thresh = 0.75
    tocheck = 5000
    shorter = 0
    for count, size in fastq_size_output(fastq_file, tocheck):
        if int(size) < min_size:
            shorter += int(count)
    return float(shorter) / float(tocheck) <= thresh