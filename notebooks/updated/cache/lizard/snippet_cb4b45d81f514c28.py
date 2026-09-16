def pythons():
    if not _pyenv_exists():
        print(
            """
pyenv is not installed. You can install it with fabsetup (https://github.com/theno/fabsetup):

    """
             + cyan(
            """mkdir ~/repos && cd ~/repos
    git clone  https://github.com/theno/fabsetup.git
    cd fabsetup  &&  fab setup.pyenv -H localhost"""
            ))
        return 1
    latest_pythons = _determine_latest_pythons()
    print(cyan('\n## install latest python versions'))
    for version in latest_pythons:
        local(flo('pyenv install --skip-existing {version}'))
    print(cyan('\n## activate pythons'))
    basedir = dirname(__file__)
    latest_pythons_str = '  '.join(latest_pythons)
    local(flo('cd {basedir}  &&  pyenv local  system  {latest_pythons_str}'))
    highest_python = latest_pythons[-1]
    print(cyan(flo(
        '\n## prepare Python-{highest_python} for testing and packaging')))
    packages_for_testing = 'pytest  tox'
    packages_for_packaging = 'pypandoc  twine'
    local(flo(
        '~/.pyenv/versions/{highest_python}/bin/pip  install --upgrade  pip  {packages_for_testing}  {packages_for_packaging}'
        ))