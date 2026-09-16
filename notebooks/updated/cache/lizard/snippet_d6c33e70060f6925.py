def _pipeline_present_with_definition(name, expected_pipeline_objects,
    expected_parameter_objects, expected_parameter_values, region, key,
    keyid, profile):
    result_pipeline_id = __salt__['boto_datapipeline.pipeline_id_from_name'](
        name, region=region, key=key, keyid=keyid, profile=profile)
    if 'error' in result_pipeline_id:
        return False, {}
    pipeline_id = result_pipeline_id['result']
    pipeline_definition_result = __salt__[
        'boto_datapipeline.get_pipeline_definition'](pipeline_id, version=
        'active', region=region, key=key, keyid=keyid, profile=profile)
    if 'error' in pipeline_definition_result:
        return False, {}
    pipeline_definition = _standardize(pipeline_definition_result['result'])
    pipeline_objects = pipeline_definition.get('pipelineObjects')
    parameter_objects = pipeline_definition.get('parameterObjects')
    parameter_values = pipeline_definition.get('parameterValues')
    present = _recursive_compare(_cleaned(pipeline_objects), _cleaned(
        expected_pipeline_objects)) and _recursive_compare(parameter_objects,
        expected_parameter_objects) and _recursive_compare(parameter_values,
        expected_parameter_values)
    return present, pipeline_definition