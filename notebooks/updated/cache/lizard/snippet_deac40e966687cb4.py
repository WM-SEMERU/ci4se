def notification(self):
    with self.selenium.context(self.selenium.CONTEXT_CHROME):
        try:
            root = self.selenium.find_element(*self._notification_locator)
            return BaseNotification.create(self, root)
        except NoSuchElementException:
            pass
        try:
            notifications = self.selenium.find_elements(*self.
                _app_menu_notification_locator)
            root = next(n for n in notifications if n.is_displayed())
            return BaseNotification.create(self, root)
        except StopIteration:
            pass
    return None