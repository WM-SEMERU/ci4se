def push_rows(self, dataset, table, rows, insert_id_key=None,
    skip_invalid_rows=None, ignore_unknown_values=None, template_suffix=
    None, project_id=None):
    project_id = self._get_project_id(project_id)
    table_data = self.bigquery.tabledata()
    rows_data = []
    for row in rows:
        each_row = {}
        each_row['json'] = row
        if insert_id_key is not None:
            keys = insert_id_key.split('.')
            val = reduce(lambda d, key: d.get(key) if d else None, keys, row)
            if val is not None:
                each_row['insertId'] = val
        rows_data.append(each_row)
    data = {'kind': 'bigquery#tableDataInsertAllRequest', 'rows': rows_data}
    if skip_invalid_rows is not None:
        data['skipInvalidRows'] = skip_invalid_rows
    if ignore_unknown_values is not None:
        data['ignoreUnknownValues'] = ignore_unknown_values
    if template_suffix is not None:
        data['templateSuffix'] = template_suffix
    try:
        response = table_data.insertAll(projectId=project_id, datasetId=
            dataset, tableId=table, body=data).execute(num_retries=self.
            num_retries)
        if response.get('insertErrors'):
            logger.error('BigQuery insert errors: %s' % response)
            if self.swallow_results:
                return False
            else:
                return response
        if self.swallow_results:
            return True
        else:
            return response
    except HttpError as e:
        logger.exception('Problem with BigQuery insertAll')
        if self.swallow_results:
            return False
        else:
            return {'insertErrors': [{'errors': [{'reason': 'httperror',
                'message': e}]}]}