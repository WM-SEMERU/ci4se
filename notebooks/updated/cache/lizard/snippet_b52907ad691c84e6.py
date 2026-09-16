def user(username, password, all):
    if current_app.config['AUTH_PROVIDER'] != 'basic':
        raise click.UsageError('Not required for {} admin users'.format(
            current_app.config['AUTH_PROVIDER']))
    if username and username not in current_app.config['ADMIN_USERS']:
        raise click.UsageError('User {} not an admin'.format(username))
    if not username and not all:
        raise click.UsageError('Missing option "--username".')

    def create_user(admin):
        email = admin if '@' in admin else None
        user = User(name='Admin user', login=admin, password=
            generate_password_hash(password), roles=['admin'], text=
            'Created by alertad script', email=email, email_verified=bool(
            email))
        try:
            db.get_db()
            user = user.create()
        except Exception as e:
            click.echo('ERROR: {}'.format(e))
        else:
            click.echo('{} {}'.format(user.id, user.name))
    if all:
        for admin in current_app.config['ADMIN_USERS']:
            create_user(admin)
    else:
        create_user(username)