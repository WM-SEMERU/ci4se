def aggregate(input, **params):
    PARAM_CFG_EXTRACT = 'extract'
    PARAM_CFG_SUBSTITUTE = 'substitute'
    PARAM_CFG_AGGREGATE = 'aggregate'
    AGGR_FIELD = 'field'
    AGGR_FUNC = 'func'
    extract_params = params.get(PARAM_CFG_EXTRACT)
    extract_params.update({AccessParams.KEY_TYPE: AccessParams.TYPE_MULTI})
    dataset = __extract(input, extract_params)
    if PARAM_CFG_SUBSTITUTE in params:
        dataset = __substitute(input, dataset, params.get(PARAM_CFG_SUBSTITUTE)
            )
    cfg = params.get(PARAM_CFG_AGGREGATE)
    res = Aggregator.agg_single_func(dataset, cfg[AGGR_FIELD], cfg[AGGR_FUNC])
    return res