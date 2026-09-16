def pipeline(stages, run=True, stride=1, chunksize=None):
    r
    from pyemma.coordinates.pipelines import Pipeline
    if not isinstance(stages, list):
        stages = [stages]
    p = Pipeline(stages, param_stride=stride, chunksize=chunksize)
    if run:
        p.parametrize()
    return p