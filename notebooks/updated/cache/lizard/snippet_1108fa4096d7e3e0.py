def get_action(self, create=False):
    action = self._widget_action
    if action is None and create:
        action = self._widget_action = QWidgetAction(None)
        action.setDefaultWidget(self.widget)
    return action