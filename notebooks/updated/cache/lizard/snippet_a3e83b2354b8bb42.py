def handle_hotmaps_results(permutation_result):
    if len(permutation_result[0]) == 6:
        mycols = ['gene', 'window length', 'codon position',
            'mutation count', 'windowed sum', 'p-value']
    else:
        mycols = ['gene', 'window length', 'codon position', 'index',
            'mutation count', 'windowed sum', 'p-value']
    permutation_df = pd.DataFrame(permutation_result, columns=mycols)
    permutation_df['q-value'] = 1
    for w in permutation_df['window length'].unique():
        is_window = permutation_df['window length'] == w
        permutation_df.loc[is_window, 'q-value'] = mypval.bh_fdr(permutation_df
            .loc[is_window, 'p-value'])
    col_order = mycols + ['q-value']
    permutation_df = permutation_df.sort_values(by=['window length', 'p-value']
        )
    return permutation_df[col_order]