def compile_file(filepath, libraries=None, combined='bin,abi', optimize=
    True, extra_args=None):
    workdir, filename = os.path.split(filepath)
    args = solc_arguments(libraries=libraries, combined=combined, optimize=
        optimize, extra_args=extra_args)
    args.insert(0, get_compiler_path())
    args.append(filename)
    output = subprocess.check_output(args, cwd=workdir)
    return solc_parse_output(output)