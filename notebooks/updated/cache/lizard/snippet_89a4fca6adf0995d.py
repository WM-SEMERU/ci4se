def run_mutect(job, tumor_bam, normal_bam, univ_options, mutect_options):
    if mutect_options['chromosomes']:
        chromosomes = mutect_options['chromosomes']
    else:
        chromosomes = sample_chromosomes(job, mutect_options['genome_fai'])
    perchrom_mutect = defaultdict()
    for chrom in chromosomes:
        perchrom_mutect[chrom] = job.addChildJobFn(run_mutect_perchrom,
            tumor_bam, normal_bam, univ_options, mutect_options, chrom,
            memory='6G', disk=PromisedRequirement(mutect_disk, tumor_bam[
            'tumor_dna_fix_pg_sorted.bam'], normal_bam[
            'normal_dna_fix_pg_sorted.bam'], mutect_options['genome_fasta'],
            mutect_options['dbsnp_vcf'], mutect_options['cosmic_vcf'])).rv()
    return perchrom_mutect