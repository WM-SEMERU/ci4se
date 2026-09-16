def system(session):
    system_test_path = os.path.join('tests', 'system.py')
    system_test_folder_path = os.path.join('tests', 'system')
    if not os.environ.get('GOOGLE_APPLICATION_CREDENTIALS', ''):
        session.skip('Credentials must be set via environment variable')
    system_test_exists = os.path.exists(system_test_path)
    system_test_folder_exists = os.path.exists(system_test_folder_path)
    if not system_test_exists and not system_test_folder_exists:
        session.skip('System tests were not found')
    session.install('--pre', 'grpcio')
    session.install('mock', 'pytest')
    for local_dep in LOCAL_DEPS:
        session.install('-e', local_dep)
    session.install('-e', '../test_utils/')
    session.install('-e', '.')
    if system_test_exists:
        session.run('py.test', '--quiet', system_test_path, *session.posargs)
    if system_test_folder_exists:
        session.run('py.test', '--quiet', system_test_folder_path, *session
            .posargs)