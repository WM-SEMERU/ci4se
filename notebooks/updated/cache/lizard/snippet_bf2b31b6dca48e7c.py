def genie3(expression_data, gene_names=None, tf_names='all',
    client_or_address='local', limit=None, seed=None, verbose=False):
    return diy(expression_data=expression_data, regressor_type='RF',
        regressor_kwargs=RF_KWARGS, gene_names=gene_names, tf_names=
        tf_names, client_or_address=client_or_address, limit=limit, seed=
        seed, verbose=verbose)