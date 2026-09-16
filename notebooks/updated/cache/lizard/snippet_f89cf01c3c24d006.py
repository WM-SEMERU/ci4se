def close_hover(self, element, use_js=False):
    try:
        if use_js:
            self._js_hover('mouseout', element)
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element_with_offset(element, -100, -100)
            actions.reset_actions()
    except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
        return True