def get_log_records_arg_dict(self, node_type):
    arg_dict = {}
    if node_type == 'cn':
        arg_dict['nodeId'] = django.conf.settings.NODE_IDENTIFIER
    return arg_dict