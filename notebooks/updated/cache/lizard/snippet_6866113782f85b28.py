def _construct_operation_id(self, service_name, protorpc_method_name):
    method_name_camel = util.snake_case_to_headless_camel_case(
        protorpc_method_name)
    return '{0}_{1}'.format(service_name, method_name_camel)