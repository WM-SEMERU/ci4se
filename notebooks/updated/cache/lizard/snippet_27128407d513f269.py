def get_output_dict(stack):
    outputs = {}
    if 'Outputs' not in stack:
        return outputs
    for output in stack['Outputs']:
        logger.debug('    %s %s: %s', stack['StackName'], output[
            'OutputKey'], output['OutputValue'])
        outputs[output['OutputKey']] = output['OutputValue']
    return outputs