def token(ctx, opts, login, password):
    click.echo('Retrieving API token for %(login)s ... ' % {'login': click.
        style(login, bold=True)}, nl=False)
    context_msg = 'Failed to retrieve the API token!'
    with handle_api_exceptions(ctx, opts=opts, context_msg=context_msg):
        with maybe_spinner(opts):
            api_key = get_user_token(login=login, password=password)
    click.secho('OK', fg='green')
    click.echo('Your API key/token is: %(token)s' % {'token': click.style(
        api_key, fg='magenta')})
    create, has_errors = create_config_files(ctx, opts, api_key=api_key)
    if has_errors:
        click.echo()
        click.secho('Oops, please fix the errors and try again!', fg='red')
        return
    if opts.api_key != api_key:
        click.echo()
        if opts.api_key:
            click.secho(
                "Note: The above API key doesn't match what you have in your default credentials config file."
                , fg='yellow')
        elif not create:
            click.secho(
                "Note: Don't forget to put your API key in a config file, export it on the environment, or set it via -k."
                , fg='yellow')
            click.secho(
                'If you need more help please see the documentation: %(website)s'
                 % {'website': click.style(get_help_website(), bold=True)})
        click.echo()
    click.secho("You're ready to rock, let's start automating!", fg='green')