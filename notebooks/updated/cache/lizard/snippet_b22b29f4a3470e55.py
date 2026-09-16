def config_required(f):

    def new_func(obj, *args, **kwargs):
        if 'config' not in obj:
            click.echo(_style(obj.get('show_color', False),
                'Could not find a valid configuration file!', fg='red',
                bold=True))
            raise click.Abort()
        else:
            return f(obj, *args, **kwargs)
    return update_wrapper(new_func, f)