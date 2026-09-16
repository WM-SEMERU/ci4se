def _writeFASTA(self, i, image):
    if isinstance(self._titlesAlignments.readsAlignments.reads, FastqReads):
        format_ = 'fastq'
    else:
        format_ = 'fasta'
    filename = '%s/%d.%s' % (self._outputDir, i, format_)
    titleAlignments = self._titlesAlignments[image['title']]
    with open(filename, 'w') as fp:
        for titleAlignment in titleAlignments:
            fp.write(titleAlignment.read.toString(format_))
    return format_