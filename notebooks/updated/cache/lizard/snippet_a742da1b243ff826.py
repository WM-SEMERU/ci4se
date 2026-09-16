def advpng(ext_args):
    args = _ADVPNG_ARGS + [ext_args.new_filename]
    extern.run_ext(args)
    return _PNG_FORMAT