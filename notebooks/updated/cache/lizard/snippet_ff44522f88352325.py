def wait_until(predicate, success_description, timeout=10):
    start = time.time()
    while True:
        retval = predicate()
        if retval:
            return retval
        if time.time() - start > timeout:
            raise AssertionError("Didn't ever %s" % success_description)
        time.sleep(0.1)