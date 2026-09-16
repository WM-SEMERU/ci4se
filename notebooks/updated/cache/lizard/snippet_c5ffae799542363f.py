def get_tmhmm_predictions(self, tmhmm_results, custom_gene_mapping=None):
    tmhmm_dict = ssbio.protein.sequence.properties.tmhmm.parse_tmhmm_long(
        tmhmm_results)
    counter = 0
    for g in tqdm(self.genes_with_a_representative_sequence):
        if custom_gene_mapping:
            g_id = custom_gene_mapping[g.id]
        else:
            g_id = g.id
        if g_id in tmhmm_dict:
            log.debug('{}: loading TMHMM results'.format(g.id))
            if not tmhmm_dict[g_id]:
                log.error('{}: missing TMHMM results'.format(g.id))
            g.protein.representative_sequence.annotations['num_tm_helix-tmhmm'
                ] = tmhmm_dict[g_id]['num_tm_helices']
            try:
                g.protein.representative_sequence.letter_annotations['TM-tmhmm'
                    ] = tmhmm_dict[g_id]['sequence']
                counter += 1
            except TypeError:
                log.error(
                    'Gene {}, SeqProp {}: sequence length mismatch between TMHMM results and representative sequence, unable to set letter annotation'
                    .format(g_id, g.protein.representative_sequence.id))
        else:
            log.error('{}: missing TMHMM results'.format(g.id))
    log.info('{}/{}: number of genes with TMHMM predictions loaded'.format(
        counter, len(self.genes)))