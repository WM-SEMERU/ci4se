def train_weather_predictor(location='Portland, OR', years=range(2013, 2016
    ), delays=(1, 2, 3), inputs=('Min Temperature', 'Max Temperature',
    'Min Sea Level Pressure', 'Max Sea Level Pressure', 'WindDirDegrees'),
    outputs=('Max TemperatureF',), N_hidden=6, epochs=30, use_cache=False,
    verbosity=2):
    df = weather.daily(location, years=years, use_cache=use_cache,
        verbosity=verbosity).sort()
    ds = util.dataset_from_dataframe(df, normalize=False, delays=delays,
        inputs=inputs, outputs=outputs, verbosity=verbosity)
    nn = util.ann_from_ds(ds, N_hidden=N_hidden, verbosity=verbosity)
    trainer = util.build_trainer(nn, ds=ds, verbosity=verbosity)
    trainer.trainEpochs(epochs)
    columns = []
    for delay in delays:
        columns += [(inp + '[-{}]'.format(delay)) for inp in inputs]
    columns += list(outputs)
    columns += ['Predicted {}'.format(outp) for outp in outputs]
    table = [(list(i) + list(t) + list(trainer.module.activate(i))) for i,
        t in zip(trainer.ds['input'], trainer.ds['target'])]
    df = pd.DataFrame(table, columns=columns, index=df.index[max(delays):])
    return trainer, df