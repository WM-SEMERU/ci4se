def check_update(ctx, forced=False):
    try:
        if ctx.update_checked and not forced:
            return
    except AttributeError:
        update_check_file = os.path.join(dir_path, 'update_check.txt')
        today = datetime.date.today().strftime('%m/%d/%Y')
        if os.path.exists(update_check_file):
            date = open(update_check_file, 'r').read()
        else:
            date = []
        if forced or today != date:
            ctx.update_checked = True
            date = today
            with open(update_check_file, 'w') as f:
                f.write(date)
            r = requests.get('https://pypi.org/pypi/keep/json').json()
            version = r['info']['version']
            curr_version = about.__version__
            if version > curr_version:
                click.secho(
                    'Keep seems to be outdated. Current version = {}, Latest version = {}'
                    .format(curr_version, version) +
                    """

Please update with """, bold=True, fg='red')
                click.secho('\tpip3 --no-cache-dir install -U keep==' + str
                    (version), fg='green')
                click.secho('\n\n')