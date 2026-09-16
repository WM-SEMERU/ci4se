def delete_fastqs(job, fastqs):
    for fq_type in ['tumor_rna', 'tumor_dna', 'normal_dna']:
        for i in xrange(0, 2):
            job.fileStore.deleteGlobalFile(fastqs[fq_type][i])
    return None