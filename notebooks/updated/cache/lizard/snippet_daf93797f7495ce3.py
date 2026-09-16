def to_json(self, data, labels=None):
    labels = labels or dict()
    json_data = dict()
    json_data['cols'] = []
    for group_col in self.group_bys_cols:
        label = '' or as_unicode(labels[group_col])
        json_data['cols'].append({'id': group_col, 'label': label, 'type':
            'string'})
    for aggr_col in self.aggr_by_cols:
        if isinstance(aggr_col, tuple):
            label_key = aggr_col[0].__name__ + aggr_col[1]
            aggr_col = aggr_col[1]
        else:
            label_key = aggr_col
        label = '' or as_unicode(labels[label_key])
        json_data['cols'].append({'id': aggr_col, 'label': label, 'type':
            'number'})
    json_data['rows'] = []
    for item in data:
        row = {'c': []}
        if not isinstance(item[0], tuple):
            row['c'].append({'v': '{0}'.format(item[0])})
        else:
            for group_col_data in item[0]:
                row['c'].append({'v': '{0}'.format(group_col_data)})
        for col_data in item[1:]:
            if isinstance(col_data, datetime.date):
                row['c'].append({'v': '{0}'.format(col_data)})
            else:
                row['c'].append({'v': col_data})
        json_data['rows'].append(row)
    return json_data