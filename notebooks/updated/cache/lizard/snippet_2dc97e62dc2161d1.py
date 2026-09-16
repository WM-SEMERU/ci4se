def referenced_tables(self):
    tables = []
    datasets_by_project_name = {}
    for table in self._job_statistics().get('referencedTables', ()):
        t_project = table['projectId']
        ds_id = table['datasetId']
        t_dataset = datasets_by_project_name.get((t_project, ds_id))
        if t_dataset is None:
            t_dataset = DatasetReference(t_project, ds_id)
            datasets_by_project_name[t_project, ds_id] = t_dataset
        t_name = table['tableId']
        tables.append(t_dataset.table(t_name))
    return tables