def find_elements_by_partial_link_text(self, link_text):
    return self.find_elements(by=By.PARTIAL_LINK_TEXT, value=link_text)