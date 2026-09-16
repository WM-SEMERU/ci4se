def enter_text(self, locator, text, with_click=True, with_clear=False,
    with_enter=False, params=None):
    element = locator
    if not isinstance(element, WebElement):
        element = self.get_visible_element(locator, params)
    if with_click:
        self.click(element)
    actions = ActionChains(self.driver)
    if 'explorer' in self.driver.name and '@' in str(text):
        actions = BasePage.handle_at_sign_for_ie(text, actions)
    else:
        actions.send_keys_to_element(element, text)
    if with_clear:
        element.clear()
        self.click(element)
    if with_enter:
        actions.send_keys(Keys.ENTER)
    actions.perform()