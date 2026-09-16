def _assign_taxonomy_with_diamond(self, base_list, db_search_results,
    graftm_package, graftm_files):
    runner = Diamond(graftm_package.diamond_database_path(), self.args.
        threads, self.args.evalue)
    taxonomy_definition = Getaxnseq().read_taxtastic_taxonomy_and_seqinfo(open
        (graftm_package.taxtastic_taxonomy_path()), open(graftm_package.
        taxtastic_seqinfo_path()))
    results = {}
    for i, search_result in enumerate(db_search_results):
        sequence_id_to_hit = {}
        logging.debug('Running diamond on %s' % search_result.hit_fasta())
        diamond_result = runner.run(search_result.hit_fasta(),
            UnpackRawReads.PROTEIN_SEQUENCE_TYPE, daa_file_basename=
            graftm_files.diamond_assignment_output_basename(base_list[i]))
        for res in diamond_result.each([SequenceSearchResult.QUERY_ID_FIELD,
            SequenceSearchResult.HIT_ID_FIELD]):
            if res[0] in sequence_id_to_hit:
                if sequence_id_to_hit[res[0]] != res[1]:
                    raise Exception(
                        'Diamond unexpectedly gave two hits for a single query sequence for %s'
                         % res[0])
            else:
                sequence_id_to_hit[res[0]] = res[1]
        sequence_id_to_taxonomy = {}
        for seqio in SequenceIO().read_fasta_file(search_result.hit_fasta()):
            name = seqio.name
            if name in sequence_id_to_hit:
                sequence_id_to_taxonomy[name] = ['Root'] + taxonomy_definition[
                    sequence_id_to_hit[name]]
            else:
                sequence_id_to_taxonomy[name] = ['Root']
        results[base_list[i]] = sequence_id_to_taxonomy
    return results