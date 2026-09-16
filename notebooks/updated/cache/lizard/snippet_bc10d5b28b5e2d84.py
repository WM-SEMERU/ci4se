def infer_dtypes(fit, model=None):
    pattern_remove_comments = re.compile(
        '//.*?$|/\\*.*?\\*/|\\\'(?:\\\\.|[^\\\\\\\'])*\\\'|"(?:\\\\.|[^\\\\"])*"'
        , re.DOTALL | re.MULTILINE)
    stan_integer = 'int'
    stan_limits = '(?:\\<[^\\>]+\\>)*'
    stan_param = '([^;=\\s\\[]+)'
    stan_ws = '\\s*'
    pattern_int = re.compile(''.join((stan_integer, stan_ws, stan_limits,
        stan_ws, stan_param)), re.IGNORECASE)
    if model is None:
        stan_code = fit.get_stancode()
        model_pars = fit.model_pars
    else:
        stan_code = model.program_code
        model_pars = fit.param_names
    stan_code = '\n'.join(line if '#' not in line else line[:line.find('#')
        ] for line in stan_code.splitlines())
    stan_code = re.sub(pattern_remove_comments, '', stan_code)
    stan_code = stan_code.split('generated quantities')[-1]
    dtypes = re.findall(pattern_int, stan_code)
    dtypes = {item.strip(): 'int' for item in dtypes if item.strip() in
        model_pars}
    return dtypes