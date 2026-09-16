def from_json_stat(datasets, naming='label', value='value'):
    warnings.warn(
        "Shouldn't use this function anymore! Now use read() methods ofDataset, Collection or Dimension."
        , DeprecationWarning)
    check_input(naming)
    results = []
    if type(datasets) is list:
        for idx, element in enumerate(datasets):
            for dataset in element:
                js_dict = datasets[idx][dataset]
                results.append(generate_df(js_dict, naming, value))
    elif isinstance(datasets, OrderedDict) or type(datasets
        ) is dict or isinstance(datasets, Dataset):
        if 'class' in datasets:
            if datasets['class'] == 'dataset':
                js_dict = datasets
                results.append(generate_df(js_dict, naming, value))
        else:
            for dataset in datasets:
                js_dict = datasets[dataset]
                results.append(generate_df(js_dict, naming, value))
    return results