def get_function_help(function: str, bel_spec: BELSpec):
    function_long = bel_spec['functions']['to_long'].get(function)
    function_help = []
    if function_long:
        for signature in bel_spec['functions']['signatures'][function_long][
            'signatures']:
            function_help.append({'function_summary': signature[
                'argument_summary'], 'argument_help': signature[
                'argument_help_listing'], 'description': bel_spec[
                'functions']['info'][function_long]['description']})
    return function_help