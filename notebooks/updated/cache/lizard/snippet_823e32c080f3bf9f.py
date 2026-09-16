def find_write(driver, elem_path, write_str, clear_first=True, send_enter=
    False, by=CSS, timeout=TIMEOUT, poll_frequency=0.5):
    elem = find_element(driver, elem_path=elem_path, by=by, timeout=timeout,
        poll_frequency=poll_frequency)
    if clear_first:
        elem.clear()
    elem.send_keys(write_str)
    if send_enter:
        elem.send_keys(Keys.ENTER)
    return elem