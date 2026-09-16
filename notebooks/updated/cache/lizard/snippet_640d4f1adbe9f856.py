def remove_armstrong():
    from pip.util import get_installed_distributions
    pkgs = get_installed_distributions(local_only=True, include_editables=True)
    apps = [pkg for pkg in pkgs if pkg.key.startswith('armstrong') and pkg.
        key != 'armstrong.dev']
    for app in apps:
        run('pip uninstall -y %s' % app.key)
    if apps:
        print(
            "Note: this hasn't removed other dependencies installed by these components. There's no substitute for a fresh virtualenv."
            )
    else:
        print('No Armstrong components to remove.')