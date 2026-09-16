def render(engine, format, filepath, renderer=None, formatter=None, quiet=False
    ):
    cmd, rendered = command(engine, format, filepath, renderer, formatter)
    run(cmd, capture_output=True, check=True, quiet=quiet)
    return rendered