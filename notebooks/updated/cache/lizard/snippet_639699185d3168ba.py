def qa(ctx):
    header(qa.__doc__)
    with ctx.cd(ROOT):
        info('Python Static Analysis')
        flake8_results = ctx.run('flake8 bumpr', pty=True, warn=True)
        if flake8_results.failed:
            error('There is some lints to fix')
        else:
            success('No lint to fix')
        info('Ensure PyPI can render README and CHANGELOG')
        readme_results = ctx.run('python setup.py check -r -s', pty=True,
            warn=True, hide=True)
        if readme_results.failed:
            print(readme_results.stdout)
            error('README and/or CHANGELOG is not renderable by PyPI')
        else:
            success('README and CHANGELOG are renderable by PyPI')
    if flake8_results.failed or readme_results.failed:
        exit('Quality check failed', flake8_results.return_code or
            readme_results.return_code)
    success('Quality check OK')