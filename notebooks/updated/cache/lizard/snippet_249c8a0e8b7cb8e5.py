def detect_fastq_annotations(fastq_file):
    annotations = set()
    queryread = tz.first(read_fastq(fastq_file))
    for k, v in BARCODEINFO.items():
        if v.readprefix in queryread:
            annotations.add(k)
    return annotations