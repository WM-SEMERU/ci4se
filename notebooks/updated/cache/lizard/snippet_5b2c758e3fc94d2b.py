def _merge_csv_column(table, csvs):
    try:
        ensemble = is_ensemble(table['columns'])
        if ensemble:
            if len(table['columns']) == 1:
                for _name, _column in table['columns'].items():
                    _column['values'] = csvs
            elif len(table['columns']) == 2:
                _multi_column = False
                for _name, _column in table['columns'].items():
                    if isinstance(_column['number'], (int, float)):
                        col_num = cast_int(_column['number'])
                        _column['values'] = csvs[col_num - 1]
                    elif isinstance(_column['number'], list):
                        if _multi_column:
                            raise Exception(
                                """Error: merge_csv_column: This jsonld metadata looks wrong!
	An ensemble table depth should not reference multiple columns of CSV data.
	Please manually fix the ensemble columns in 'metadata.jsonld' inside of your LiPD file."""
                                )
                        else:
                            _multi_column = True
                            _column['values'] = csvs[2:]
        else:
            for _name, _column in table['columns'].items():
                col_num = cast_int(_column['number'])
                _column['values'] = csvs[col_num - 1]
    except IndexError:
        logger_csvs.warning(
            'merge_csv_column: IndexError: index out of range of csv_data list'
            )
    except KeyError:
        logger_csvs.error('merge_csv_column: KeyError: missing columns key')
    except Exception as e:
        logger_csvs.error('merge_csv_column: Unknown Error:  {}'.format(e))
        print('Quitting...')
        exit(1)
    return table, ensemble