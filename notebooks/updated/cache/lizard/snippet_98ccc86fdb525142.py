def count_mapped_reads(self, file_name, paired_end):
    if file_name.endswith('bam'):
        return self.samtools_view(file_name, param='-c -F4')
    if file_name.endswith('sam'):
        return self.samtools_view(file_name, param='-c -F4 -S')
    return -1