def load_extra_emacs_page_navigation_bindings():
    registry = ConditionalRegistry(Registry(), EmacsMode())
    handle = registry.add_binding
    handle(Keys.ControlV)(scroll_page_down)
    handle(Keys.PageDown)(scroll_page_down)
    handle(Keys.Escape, 'v')(scroll_page_up)
    handle(Keys.PageUp)(scroll_page_up)
    return registry