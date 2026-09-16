def wait_and_ignore(condition, timeout=WTF_TIMEOUT_MANAGER.NORMAL, sleep=0.5):
    try:
        return wait_until(condition, timeout, sleep)
    except:
        pass