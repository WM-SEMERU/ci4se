def _create_genome_regions(data):
    work_dir = utils.safe_makedir(os.path.join(dd.get_work_dir(data),
        'coverage', dd.get_sample_name(data)))
    variant_regions = os.path.join(work_dir, 'target-genome.bed')
    with file_transaction(data, variant_regions) as tx_variant_regions:
        with open(tx_variant_regions, 'w') as out_handle:
            for c in shared.get_noalt_contigs(data):
                out_handle.write('%s\t%s\t%s\n' % (c.name, 0, c.size))
    return variant_regions