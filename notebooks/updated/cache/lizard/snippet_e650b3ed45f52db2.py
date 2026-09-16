def GetBigQueryClient(service_account_json=None, project_id=None,
    dataset_id=None):
    service_account_data = service_account_json or config.CONFIG[
        'BigQuery.service_acct_json']
    project_id = project_id or config.CONFIG['BigQuery.project_id']
    dataset_id = dataset_id or config.CONFIG['BigQuery.dataset_id']
    if not (service_account_data and project_id and dataset_id):
        raise RuntimeError(
            'BigQuery.service_account_json, BigQuery.project_id and BigQuery.dataset_id must be defined.'
            )
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.Parse(
        service_account_data), scopes=BIGQUERY_SCOPE)
    http_obj = httplib2.Http()
    http_obj = creds.authorize(http_obj)
    service = discovery.build('bigquery', 'v2', http=http_obj)
    return BigQueryClient(project_id=project_id, bq_service=service,
        dataset_id=dataset_id)