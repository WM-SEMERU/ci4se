def dca(adata, mode='denoise', ae_type='zinb-conddisp', normalize_per_cell=
    True, scale=True, log1p=True, hidden_size=(64, 32, 64), hidden_dropout=
    0.0, batchnorm=True, activation='relu', init='glorot_uniform',
    network_kwds={}, epochs=300, reduce_lr=10, early_stop=15, batch_size=32,
    optimizer='rmsprop', random_state=0, threads=None, verbose=False,
    training_kwds={}, return_model=False, return_info=False, copy=False):
    try:
        from dca.api import dca
    except ImportError:
        raise ImportError(
            'Please install dca package (>= 0.2.1) via `pip install dca`')
    return dca(adata, mode=mode, ae_type=ae_type, normalize_per_cell=
        normalize_per_cell, scale=scale, log1p=log1p, hidden_size=
        hidden_size, hidden_dropout=hidden_dropout, batchnorm=batchnorm,
        activation=activation, init=init, network_kwds=network_kwds, epochs
        =epochs, reduce_lr=reduce_lr, early_stop=early_stop, batch_size=
        batch_size, optimizer=optimizer, random_state=random_state, threads
        =threads, verbose=verbose, training_kwds=training_kwds,
        return_model=return_model)