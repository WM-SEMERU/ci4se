def import_sip04_data_all(data_filename):
    filename, fformat = os.path.splitext(data_filename)
    if fformat == '.csv':
        print('Import SIP04 data from .csv file')
        df_all = _import_csv_file(data_filename)
    elif fformat == '.mat':
        print('Import SIP04 data from .mat file')
        df_all = _import_mat_file(data_filename)
    else:
        print('Please use .csv or .mat format.')
        df_all = None
    return df_all