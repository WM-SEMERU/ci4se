def update_lipd_v1_1(d):
    logger_versions.info('enter update_lipd_v1_1')
    tmp_all = []
    try:
        if 'chronData' in d:
            for table in d['chronData']:
                if 'chronMeasurementTable' not in table:
                    tmp_all.append({'chronMeasurementTable': [table]})
                elif 'chronMeasurementTable' in table:
                    if isinstance(table['chronMeasurementTable'], dict):
                        tmp_all.append({'chronMeasurementTable': [table[
                            'chronMeasurementTable']]})
            if tmp_all:
                d['chronData'] = tmp_all
        d['lipdVersion'] = 1.1
    except Exception as e:
        logger_versions.error('update_lipd_v1_1: Exception: {}'.format(e))
    logger_versions.info('exit update_lipd_v1_1')
    return d