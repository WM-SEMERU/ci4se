def find(self, locator, find_all=False, search_object=None, force_find=
    False, exclude_invisible=False):
    search_object = self.driver if search_object is None else search_object
    attempts = 0
    while attempts < self.find_attempts + 1:
        if bool(force_find):
            js_locator = self.locator_handler.parse_locator(locator)
            if js_locator.By != 'css selector':
                raise ValueError(
                    'You must use a css locator in order to force find an element; this was "{}"'
                    .format(js_locator))
            elements = self.js_executor.execute_template_and_return_result(
                'getElementsTemplate.js', variables={'selector': js_locator
                .value})
        else:
            elements = self.locator_handler.find_by_locator(search_object,
                locator, True)
        all_elements = elements
        visible_elements = elements
        if exclude_invisible:
            visible_elements = [element for element in all_elements if
                element.is_displayed()]
            elements = visible_elements
        if len(elements) > 0:
            if find_all is True:
                for index in range(len(elements)):
                    elements[index] = WebElementWrapper.WebElementWrapper(self,
                        locator, elements[index], search_object=search_object)
                return elements
            elif find_all is False:
                return WebElementWrapper.WebElementWrapper(self, locator,
                    elements[0], search_object=search_object)
        elif attempts >= self.find_attempts:
            if find_all is True:
                return []
            else:
                error_message = (
                    'Unable to find element after {0} attempts with locator: {1}'
                    .format(attempts, locator))
                if exclude_invisible and len(visible_elements) == 0 and len(
                    all_elements) > 0:
                    error_message = (
                        'Elements found using locator {}, but none were visible'
                        .format(locator))
                raise WebDriverWrapperException.WebDriverWrapperException(self,
                    error_message)
        else:
            attempts += 1