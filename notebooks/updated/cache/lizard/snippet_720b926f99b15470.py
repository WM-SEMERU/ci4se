def run_numerical_analysis(table, schema_list, args):
    import google.datalab.bigquery as bq
    numerical_columns = []
    for col_schema in schema_list:
        col_type = col_schema['type'].lower()
        if col_type == 'integer' or col_type == 'float':
            numerical_columns.append(col_schema['name'])
    if numerical_columns:
        sys.stdout.write('Running numerical analysis...')
        max_min = [
            'max({name}) as max_{name}, min({name}) as min_{name}, avg({name}) as avg_{name} '
            .format(name=name) for name in numerical_columns]
        if args.bigquery_table:
            sql = 'SELECT  %s from `%s`' % (', '.join(max_min),
                parse_table_name(args.bigquery_table))
            numerical_results = bq.Query(sql).execute().result().to_dataframe()
        else:
            sql = 'SELECT  %s from csv_table' % ', '.join(max_min)
            query = bq.Query(sql, data_sources={'csv_table': table})
            numerical_results = query.execute().result().to_dataframe()
        results_dict = {}
        for name in numerical_columns:
            results_dict[name] = {'max': numerical_results.iloc[0]['max_%s' %
                name], 'min': numerical_results.iloc[0]['min_%s' % name],
                'mean': numerical_results.iloc[0]['avg_%s' % name]}
        file_io.write_string_to_file(os.path.join(args.output_dir,
            NUMERICAL_ANALYSIS_FILE), json.dumps(results_dict, indent=2,
            separators=(',', ': ')))
        sys.stdout.write('done.\n')