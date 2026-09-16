def find_element_by_link_text(self, link_text):
    return self.find_element(by=By.LINK_TEXT, value=link_text)