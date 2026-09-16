def check_python_matlab_architecture(bits, lib_dir):
    if not os.path.isdir(lib_dir):
        raise RuntimeError(
            "It seem that you are using {bits} version of Python, but there's no matching MATLAB installation in {lib_dir}."
            .format(bits=bits, lib_dir=lib_dir))