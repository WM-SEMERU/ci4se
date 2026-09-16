def assert_checked_checkbox(self, value):
    check_box = find_field(world.browser, 'checkbox', value)
    assert check_box, "Cannot find checkbox '{}'.".format(value)
    assert check_box.is_selected(), 'Check box should be selected.'