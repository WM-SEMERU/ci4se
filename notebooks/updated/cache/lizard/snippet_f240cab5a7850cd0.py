def _raise_error_if_column_exists(dataset, column_name='dataset',
    dataset_variable_name='dataset', column_name_error_message_name=
    'column_name'):
    err_msg = 'The SFrame {0} must contain the column {1}.'.format(
        dataset_variable_name, column_name_error_message_name)
    if column_name not in dataset.column_names():
        raise ToolkitError(str(err_msg))