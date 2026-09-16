def step_command_output_should_contain_log_records_from_categories(context):
    assert context.table, 'REQUIRE: context.table'
    context.table.require_column('category')
    record_schema = context.log_record_row_schema
    LogRecordTable.annotate_with_row_schema(context.table, record_schema)
    step_command_output_should_contain_log_records(context)
    context.table.remove_columns(['level', 'message'])