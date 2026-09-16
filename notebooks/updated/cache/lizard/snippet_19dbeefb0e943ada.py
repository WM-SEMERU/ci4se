def kegg_mapping_and_metadata(self, kegg_organism_code, custom_gene_mapping
    =None, outdir=None, set_as_representative=False, force_rerun=False):
    kegg_to_uniprot = ssbio.databases.kegg.map_kegg_all_genes(organism_code
        =kegg_organism_code, target_db='uniprot')
    successfully_mapped_counter = 0
    for g in tqdm(self.genes):
        if custom_gene_mapping:
            kegg_g = custom_gene_mapping[g.id]
        else:
            kegg_g = g.id
        if kegg_g not in kegg_to_uniprot:
            log.debug('{}: unable to map to KEGG'.format(g.id))
            continue
        kegg_prop = g.protein.load_kegg(kegg_id=kegg_g, kegg_organism_code=
            kegg_organism_code, download=True, outdir=outdir,
            set_as_representative=set_as_representative, force_rerun=
            force_rerun)
        if kegg_g in kegg_to_uniprot.keys():
            kegg_prop.uniprot = kegg_to_uniprot[kegg_g]
            if g.protein.representative_sequence:
                if g.protein.representative_sequence.kegg == kegg_prop.kegg:
                    g.protein.representative_sequence.uniprot = (
                        kegg_to_uniprot[kegg_g])
        if kegg_prop.sequence_file:
            successfully_mapped_counter += 1
        log.debug('{}: loaded KEGG information for gene'.format(g.id))
    log.info('{}/{}: number of genes mapped to KEGG'.format(
        successfully_mapped_counter, len(self.genes)))
    log.info(
        'Completed ID mapping --> KEGG. See the "df_kegg_metadata" attribute for a summary dataframe.'
        )