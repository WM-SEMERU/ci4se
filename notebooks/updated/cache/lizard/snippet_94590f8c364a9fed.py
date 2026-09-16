def _get_step_inout(step):
    inputs = []
    outputs = []
    assert step.inputs_record_schema['type'] == 'record'
    for inp in step.inputs_record_schema['fields']:
        source = inp['source'].split('#')[-1].replace('/', '.')
        if 'valueFrom' in inp:
            attr_access = "['%s']" % inp['name']
            if inp['valueFrom'].find(attr_access) > 0:
                source += '.%s' % inp['name']
        inputs.append({'id': inp['name'], 'value': source})
    assert step.outputs_record_schema['type'] == 'record'
    for outp in step.outputs_record_schema['fields']:
        outputs.append({'id': outp['name']})
    return inputs, outputs