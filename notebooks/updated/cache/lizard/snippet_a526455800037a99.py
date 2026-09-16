def batch(ctx, path, recursive, watch):
    batch = Batch(ctx.obj['config'], ctx.obj['cucco'])
    if os.path.exists(path):
        if watch:
            batch.watch(path, recursive)
        elif os.path.isfile(path):
            batch.process_file(path)
        else:
            batch.process_files(path, recursive)
    else:
        click.echo("Error: Specified path doesn't exists", err=True)
        sys.exit(-1)