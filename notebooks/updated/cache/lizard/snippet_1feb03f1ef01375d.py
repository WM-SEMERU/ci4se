def df_pdb_ranking(self):
    best_structures_pre_df = []
    chain_specific_keys = ['coverage', 'start', 'end', 'unp_start',
        'unp_end', 'rank']
    for p in self.get_experimental_structures():
        for c in p.chains:
            if hasattr(c, 'rank'):
                infodict = p.get_dict_with_chain(chain=c.id, df_format=True,
                    chain_keys=chain_specific_keys)
                infodict['pdb_id'] = p.id
                infodict['pdb_chain_id'] = c.id
                infodict['uniprot'] = self.representative_sequence.uniprot
                best_structures_pre_df.append(infodict)
    cols = ['uniprot', 'pdb_id', 'pdb_chain_id', 'experimental_method',
        'resolution', 'coverage', 'taxonomy_name', 'start', 'end',
        'unp_start', 'unp_end', 'rank']
    df = pd.DataFrame.from_records(best_structures_pre_df, columns=cols
        ).set_index(['pdb_id', 'pdb_chain_id'])
    return ssbio.utils.clean_df(df)