def execute_query_return_result_proxy(query):
    context = query._compile_context()
    context.statement.use_labels = False
    if query._autoflush and not query._populate_existing:
        query.session._autoflush()
    conn = query._get_bind_args(context, query._connection_from_session,
        close_with_result=True)
    return conn.execute(context.statement, query._params)