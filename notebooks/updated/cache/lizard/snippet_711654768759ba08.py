def bbknn(adata, batch_key='batch', save_knn=False, copy=False, **kwargs):
    params = locals()
    kwargs = params.pop('kwargs')
    try:
        from bbknn import bbknn
    except ImportError:
        raise ImportError('Please install bbknn: `pip install bbknn`.')
    return bbknn(**params, **kwargs)