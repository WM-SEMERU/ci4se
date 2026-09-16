def reload(script, input, output):
    script = Path(script).expand().abspath()
    output = Path(output).expand().abspath()
    input = input if isinstance(input, (list, tuple)) else [input]
    output.makedirs_p()
    _script_reload(script, input, output)