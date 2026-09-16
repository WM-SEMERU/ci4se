def _do_analysis(options):
    module = _function_location(options)
    core_results = _call_analysis_function(options, module)
    if module == 'emp' and 'models' in options.keys():
        fit_results = _fit_models(options, core_results)
    else:
        fit_results = None
    _save_results(options, module, core_results, fit_results)