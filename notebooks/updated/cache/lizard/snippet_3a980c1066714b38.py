def make_db_data_fetcher(postgresql_conn_info, template_path,
    reload_templates, query_cfg, io_pool):
    sources = parse_source_data(query_cfg)
    queries_generator = make_queries_generator(sources, template_path,
        reload_templates)
    return DataFetcher(postgresql_conn_info, queries_generator, io_pool)