def __get_form_data(self, soup):
    elements = self.__get_valid_form_data_elements(soup)
    form_data = self.__get_default_form_data_input(elements)
    callback = self.options.callbacks.form_before_autofill
    action = callback(self.queue_item, elements, form_data)
    if action == CrawlerActions.DO_AUTOFILL_FORM:
        self.__autofill_form_data(form_data, elements)
    return form_data