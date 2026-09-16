def make(directory):
    if os.path.exists(directory):
        if os.path.isdir(directory):
            click.echo('Directory already exists')
        else:
            click.echo('Path exists and is not a directory')
        sys.exit()
    os.makedirs(directory)
    os.mkdir(os.path.join(directory, 'jsons'))
    copy_default_config(os.path.join(directory, 'config.yaml'))