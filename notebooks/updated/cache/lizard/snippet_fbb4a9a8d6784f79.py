def ParseOptions(cls, options, configuration_object):
    if not isinstance(configuration_object, tools.CLITool):
        raise errors.BadConfigObject(
            'Configuration object is not an instance of CLITool')
    filter_collection = getattr(configuration_object, '_filter_collection',
        None)
    if not filter_collection:
        raise errors.BadConfigObject(
            'Filter collection missing from configuration object')
    date_filters = getattr(options, 'date_filters', None)
    if not date_filters:
        return
    file_entry_filter = file_entry_filters.DateTimeFileEntryFilter()
    for date_filter in date_filters:
        date_filter_pieces = date_filter.split(',')
        if len(date_filter_pieces) != 3:
            raise errors.BadConfigOption('Badly formed date filter: {0:s}'.
                format(date_filter))
        time_value, start_time_string, end_time_string = date_filter_pieces
        time_value = time_value.strip()
        start_time_string = start_time_string.strip()
        end_time_string = end_time_string.strip()
        try:
            file_entry_filter.AddDateTimeRange(time_value,
                start_time_string=start_time_string, end_time_string=
                end_time_string)
        except ValueError:
            raise errors.BadConfigOption('Badly formed date filter: {0:s}'.
                format(date_filter))
    filter_collection.AddFilter(file_entry_filter)