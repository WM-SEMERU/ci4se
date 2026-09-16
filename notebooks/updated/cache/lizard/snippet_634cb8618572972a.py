def _execute_cell(args, cell_body):
    query = _get_query_argument(args, cell_body, datalab.utils.commands.
        notebook_environment())
    if args['verbose']:
        print(query.sql)
    return query.execute(args['target'], table_mode=args['mode'], use_cache
        =not args['nocache'], allow_large_results=args['large'], dialect=
        args['dialect'], billing_tier=args['billing']).results