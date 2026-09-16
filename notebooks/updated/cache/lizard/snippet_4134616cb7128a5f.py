def do_check_pep8(files, status):
    for file_name in files:
        args = ['flake8', '--max-line-length=120', '{0}'.format(file_name)]
        output = run(*args)
        if output:
            status.append('Python PEP8/Flake8: {0}: {1}'.format(file_name,
                output))
    return status