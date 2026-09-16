def task_list(limit, filter_task_id, filter_status, filter_type,
    filter_label, filter_not_label, inexact, filter_requested_after,
    filter_requested_before, filter_completed_after, filter_completed_before):

    def _process_filterval(prefix, value, default=None):
        if value:
            if isinstance(value, six.string_types):
                return '{}:{}/'.format(prefix, value)
            return '{}:{}/'.format(prefix, ','.join(str(x) for x in value))
        else:
            return default or ''
    filter_string = ''
    filter_string += _process_filterval('task_id', filter_task_id)
    filter_string += _process_filterval('status', filter_status)
    filter_string += _process_filterval('type', filter_type, default=
        'type:TRANSFER,DELETE/')
    if inexact:
        label_data = [('~' + s) for s in filter_label] + [('!~' + s) for s in
            filter_not_label]
    else:
        label_data = [('=' + s) for s in filter_label] + [('!' + s) for s in
            filter_not_label]
    filter_string += _process_filterval('label', label_data)
    filter_string += _process_filterval('request_time', [
        filter_requested_after or '', filter_requested_before or ''])
    filter_string += _process_filterval('completion_time', [
        filter_completed_after or '', filter_completed_before or ''])
    client = get_client()
    task_iterator = client.task_list(num_results=limit, filter=
        filter_string[:-1])
    fields = [('Task ID', 'task_id'), ('Status', 'status'), ('Type', 'type'
        ), ('Source Display Name', 'source_endpoint_display_name'), (
        'Dest Display Name', 'destination_endpoint_display_name'), ('Label',
        'label')]
    formatted_print(task_iterator, fields=fields, json_converter=
        iterable_response_to_dict)