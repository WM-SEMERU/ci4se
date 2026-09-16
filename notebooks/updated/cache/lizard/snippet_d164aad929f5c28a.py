def element_id_by_label(browser, label):
    label = ElementSelector(browser, str('//label[contains(., %s)]' %
        string_literal(label)))
    if not label:
        return False
    return label.get_attribute('for')