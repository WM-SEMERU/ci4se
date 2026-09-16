def get_widget(name):
    for widget in registry:
        if widget.__name__ == name:
            return widget
    raise WidgetNotFound(_('The widget %s has not been registered.') % name)