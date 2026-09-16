def validate(D, detailed=True):
    start = clock()
    print('\n')
    print(
        'Fetching results from validator at lipd.net/validator... this may take a few moments.\n'
        )
    try:
        results = []
        if 'paleoData' in D:
            _api_data = get_validator_format(D)
            results.append(call_validator_api(D['dataSetName'], _api_data))
        else:
            for dsn, dat in D.items():
                _api_data = get_validator_format(dat)
                results.append(call_validator_api(dsn, _api_data))
        display_results(results, detailed)
    except Exception as e:
        print('Error: validate: {}'.format(e))
    end = clock()
    logger_benchmark.info(log_benchmark('validate', start, end))
    return