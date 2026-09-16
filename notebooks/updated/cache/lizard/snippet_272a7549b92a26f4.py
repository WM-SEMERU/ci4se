def infer_genome_from_vcf(genome, vcf_reader, reference_vcf_key):
    if genome:
        return infer_genome(genome)
    elif reference_vcf_key not in vcf_reader.metadata:
        raise ValueError('Unable to infer reference genome for %s' % (
            vcf_reader.filename,))
    else:
        reference_path = vcf_reader.metadata[reference_vcf_key]
        return infer_genome(reference_path)