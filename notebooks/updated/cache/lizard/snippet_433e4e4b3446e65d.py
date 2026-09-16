def get_sgburst_waveform(template=None, **kwargs):
    input_params = props_sgburst(template, **kwargs)
    for arg in sgburst_required_args:
        if arg not in input_params:
            raise ValueError('Please provide ' + str(arg))
    return _lalsim_sgburst_waveform(**input_params)