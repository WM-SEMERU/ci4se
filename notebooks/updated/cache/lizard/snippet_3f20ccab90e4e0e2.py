def pypi():
    if not query_yes_no('version updated in `fabsetup/_version.py`?'):
        print('abort')
    else:
        print(cyan('\n## clean-up\n'))
        execute(clean)
        basedir = dirname(__file__)
        python = 'python'
        print(cyan('\n## build package'))
        local(flo('cd {basedir}  &&  {python}  setup.py  sdist'))
        print(cyan('\n## upload package'))
        local(flo('cd {basedir}  &&  {python} -m twine upload  dist/*'))