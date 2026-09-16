def check_service_windows(pfeed, *, as_df=False, include_warnings=False):
    table = 'service_windows'
    problems = []
    if pfeed.service_windows is None:
        problems.append(['error', 'Missing table', table, []])
    else:
        f = pfeed.service_windows.copy()
        problems = check_for_required_columns(problems, table, f)
    if problems:
        return gt.format_problems(problems, as_df=as_df)
    if include_warnings:
        problems = check_for_invalid_columns(problems, table, f)
    problems = gt.check_column_id(problems, table, f, 'service_window_id')
    for column in ['start_time', 'end_time']:
        problems = gt.check_column(problems, table, f, column, gt.valid_time)
    v = lambda x: x in range(2)
    for col in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday', 'sunday']:
        problems = gt.check_column(problems, table, f, col, v)
    return gt.format_problems(problems, as_df=as_df)