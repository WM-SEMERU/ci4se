def get_risk_files(inputs):
    rfs = {}
    job_ini = inputs['job_ini']
    for key in inputs:
        if key == 'fragility':
            rfs['fragility/structural'] = inputs['structural_fragility'
                ] = inputs[key]
            del inputs['fragility']
        elif key.endswith(('_fragility', '_vulnerability', '_consequence')):
            match = RISK_TYPE_REGEX.match(key)
            if match and 'retrofitted' not in key and 'consequence' not in key:
                rfs['%s/%s' % (match.group(2), match.group(1))] = inputs[key]
            elif match is None:
                raise ValueError('Invalid key in %s: %s_file' % (job_ini, key))
    return rfs