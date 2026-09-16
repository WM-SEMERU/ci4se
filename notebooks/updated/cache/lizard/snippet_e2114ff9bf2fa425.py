def default(session):
    session.install('mock', 'pytest', 'pytest-cov')
    for local_dep in LOCAL_DEPS:
        session.install('-e', local_dep)
    dev_install = '.[all]'
    session.install('-e', dev_install)
    if session.python == '2.7':
        session.install('ipython==5.5')
    else:
        session.install('ipython')
    session.run('py.test', '--quiet', '--cov=google.cloud.bigquery',
        '--cov=tests.unit', '--cov-append', '--cov-config=.coveragerc',
        '--cov-report=', '--cov-fail-under=97', os.path.join('tests',
        'unit'), *session.posargs)