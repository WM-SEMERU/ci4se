def register_widget(widget):
    if widget in registry:
        raise WidgetAlreadyRegistered(_(
            'The widget %s has already been registered.') % widget.__name__)
    registry.append(widget)