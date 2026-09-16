def select_by_visible_text(self, text):
    xpath = './/option[normalize-space(.) = {0}]'.format(self.
        _escape_string(text))
    opts = self.find_elements_by_xpath(xpath)
    matched = False
    for opt in opts:
        self._set_selected(opt)
        if not self.is_multiple:
            return
        matched = True
    if len(opts) == 0 and ' ' in text:
        sub_string_without_space = self._get_longest_token(text)
        if sub_string_without_space == '':
            candidates = self.get_options()
        else:
            xpath = './/option[contains(.,{0})]'.format(self._escape_string
                (sub_string_without_space))
            candidates = self.find_elements_by_xpath(xpath)
        for candidate in candidates:
            if text == candidate.text:
                self._set_selected(candidate)
                if not self.is_multiple:
                    return
                matched = True
    if not matched:
        raise NoSuchElementException(
            'Could not locate element with visible text: ' + str(text))