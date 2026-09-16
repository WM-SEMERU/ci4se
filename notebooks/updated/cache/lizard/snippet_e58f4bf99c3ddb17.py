def wait_for_text(self, locator, text):
    for i in range(timeout_seconds):
        try:
            e = self.driver.find_element_by_locator(locator)
            if e.text == text:
                break
        except:
            pass
        time.sleep(1)
    else:
        raise ElementTextTimeout('%s value timed out' % locator)
    return True