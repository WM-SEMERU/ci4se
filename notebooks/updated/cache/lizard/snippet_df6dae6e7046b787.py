def semaphore(branch: str):
    assert os.environ.get('BRANCH_NAME') == branch
    assert os.environ.get('PULL_REQUEST_NUMBER') is None
    assert os.environ.get('SEMAPHORE_THREAD_RESULT') != 'failed'