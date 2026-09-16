def _ctypes_ex_variables(executable):
    result = []
    for p in executable.ordered_parameters:
        _ctypes_code_parameter(result, p, 'indices')
        _ctypes_code_parameter(result, p, 'variable')
        _ctypes_code_parameter(result, p, 'out')
    if type(executable).__name__ == 'Function':
        _ctypes_code_parameter(result, executable, 'indices')
        _ctypes_code_parameter(result, executable, 'variable')
        _ctypes_code_parameter(result, executable, 'out')
    return result