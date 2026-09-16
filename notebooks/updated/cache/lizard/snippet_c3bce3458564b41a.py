def uniprot_reviewed_checker(uniprot_id):
    query_string = 'id:' + uniprot_id
    uni_rev_raw = StringIO(bsup.search(query_string, columns='id,reviewed',
        frmt='tab'))
    uni_rev_df = pd.read_table(uni_rev_raw, sep='\t', index_col=0)
    uni_rev_df = uni_rev_df.fillna(False)
    uni_rev_df = uni_rev_df[pd.notnull(uni_rev_df.Status)]
    uni_rev_df = uni_rev_df.replace(to_replace='reviewed', value=True)
    uni_rev_df = uni_rev_df.replace(to_replace='unreviewed', value=False)
    uni_rev_dict_adder = uni_rev_df.to_dict()['Status']
    return uni_rev_dict_adder[uniprot_id]