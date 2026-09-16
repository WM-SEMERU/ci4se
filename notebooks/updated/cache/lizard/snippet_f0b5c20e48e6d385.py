def compile_file_into_spirv(filepath, stage, optimization='size',
    warnings_as_errors=False):
    with open(filepath, 'rb') as f:
        content = f.read()
    return compile_into_spirv(content, stage, filepath, optimization=
        optimization, warnings_as_errors=warnings_as_errors)