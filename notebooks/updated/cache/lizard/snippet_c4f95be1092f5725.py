def wait_until_internet(time_between_attempts=3, max_attempts=10):
    counter = 0
    while not is_internet_on():
        time.sleep(time_between_attempts)
        counter += 1
        if counter > max_attempts:
            return False
    return True