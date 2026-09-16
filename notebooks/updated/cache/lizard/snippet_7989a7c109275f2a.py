def handle_tsg_results(permutation_result):
    permutation_df = pd.DataFrame(sorted(permutation_result, key=lambda x: 
        x[2] if x[2] is not None else 1.1), columns=['gene',
        'inactivating count', 'inactivating p-value', 'Total SNV Mutations',
        'SNVs Unmapped to Ref Tx'])
    permutation_df['inactivating p-value'] = permutation_df[
        'inactivating p-value'].astype('float')
    tmp_df = permutation_df[permutation_df['inactivating p-value'].notnull()]
    permutation_df['inactivating BH q-value'] = np.nan
    permutation_df.loc[tmp_df.index, 'inactivating BH q-value'
        ] = mypval.bh_fdr(tmp_df['inactivating p-value'])
    permutation_df = permutation_df.sort_values(by='inactivating p-value',
        ascending=False)
    permutation_df = permutation_df.reindex(index=permutation_df.index[::-1])
    permutation_df = permutation_df.set_index('gene', drop=False)
    col_order = ['gene', 'Total SNV Mutations', 'SNVs Unmapped to Ref Tx',
        'inactivating count', 'inactivating p-value', 'inactivating BH q-value'
        ]
    return permutation_df[col_order]