def _build_final_method_name(method_name, dataset_name, dataprovider_name,
    repeat_suffix):
    suffix = ''
    if dataprovider_name:
        suffix = '_{0}'.format(dataprovider_name)
    if not dataset_name and not repeat_suffix:
        return '{0}{1}'.format(method_name, suffix)
    if dataset_name:
        dataset_name = dataset_name.replace('.', REPLACE_FOR_PERIOD_CHAR)
    suffix = '{0}({1})'.format(suffix, dataset_name or '')
    if repeat_suffix:
        suffix = '{0} {1}'.format(suffix, repeat_suffix)
    test_method_name_for_dataset = '{0}{1}'.format(method_name, suffix)
    return test_method_name_for_dataset