def see_tooltip(step, tooltip):
    elem = world.browser.find_elements_by_xpath(str(
        '//*[@title="%(tooltip)s" or @data-original-title="%(tooltip)s"]' %
        dict(tooltip=tooltip)))
    elem = [e for e in elem if e.is_displayed()]
    assert_true(step, elem)