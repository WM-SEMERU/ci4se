def parse_parameter_group(self, global_params, region, parameter_group):
    pg_name = parameter_group.pop('ParameterGroupName')
    pg_id = self.get_non_aws_id(pg_name)
    parameter_group['name'] = pg_name
    parameter_group['parameters'] = {}
    api_client = api_clients[region]
    parameters = handle_truncated_response(api_client.
        describe_cluster_parameters, {'ParameterGroupName': pg_name}, [
        'Parameters'])['Parameters']
    for parameter in parameters:
        param = {}
        param['value'] = parameter['ParameterValue']
        param['source'] = parameter['Source']
        parameter_group['parameters'][parameter['ParameterName']] = param
    self.parameter_groups[pg_id] = parameter_group