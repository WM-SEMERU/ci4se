def _inherited_row(row, base_rows_from_pillar, ret):
    base_rows = []
    for base_row_from_pillar in base_rows_from_pillar:
        base_row = __salt__['pillar.get'](base_row_from_pillar)
        if base_row:
            base_rows.append(base_row)
        elif base_row_from_pillar != _DEFAULT_ROW_PILLAR:
            ret.setdefault('warnings', [])
            warning_message = 'Cannot find row pillar "{0}".'.format(
                base_row_from_pillar)
            if warning_message not in ret['warnings']:
                ret['warnings'].append(warning_message)
    base_rows.append(row)
    result_row = {}
    for row in base_rows:
        result_row.update(row)
    return result_row