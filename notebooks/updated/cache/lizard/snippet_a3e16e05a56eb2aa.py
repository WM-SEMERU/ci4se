def build(ctx):
    return_code = run_sphinx(ctx.obj['root_dir'])
    if return_code > 0:
        sys.exit(return_code)