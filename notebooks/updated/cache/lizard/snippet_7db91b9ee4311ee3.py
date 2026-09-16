def _get_csv_from_section(d, pc, csv_data):
    logger_jsons.info('enter get_csv_from_section: {}'.format(pc))
    for table, table_content in d[pc].items():
        csv_data[table_content['filename']] = OrderedDict()
        for column, column_content in table_content['columns'].items():
            csv_data[table_content['filename']][column_content['number']
                ] = column_content['values']
    logger_jsons.info('exit get_csv_from_section: {}'.format(pc))
    return csv_data