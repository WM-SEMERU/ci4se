def execute_project_models_sql_scripts(force_update=False):
    with open(MODEL_FILE, 'r') as file_content:
        query = file_content.read()
        db = db_connector()
        query_result = db.execute_pandas_sql_query(query)
        db.close()
        try:
            projects = Project.objects.bulk_create(Project(**vals) for vals in
                query_result.to_dict('records'))
            indicators = [FinancialIndicator(project=p) for p in projects]
            FinancialIndicator.objects.bulk_create(indicators)
        except IntegrityError:
            LOG('Projects bulk_create failed, creating one by one...')
            with transaction.atomic():
                if force_update:
                    for item in query_result.to_dict('records'):
                        p, _ = Project.objects.update_or_create(**item)
                        FinancialIndicator.objects.update_or_create(project=p)
                else:
                    for item in query_result.to_dict('records'):
                        p, _ = Project.objects.get_or_create(**item)
                        FinancialIndicator.objects.update_or_create(project=p)