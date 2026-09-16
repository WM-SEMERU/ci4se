def load_key_bindings(get_search_state=None, enable_abort_and_exit_bindings
    =False, enable_system_bindings=False, enable_search=False,
    enable_open_in_editor=False, enable_extra_page_navigation=False,
    enable_auto_suggest_bindings=False):
    assert get_search_state is None or callable(get_search_state)
    enable_abort_and_exit_bindings = to_cli_filter(
        enable_abort_and_exit_bindings)
    enable_system_bindings = to_cli_filter(enable_system_bindings)
    enable_search = to_cli_filter(enable_search)
    enable_open_in_editor = to_cli_filter(enable_open_in_editor)
    enable_extra_page_navigation = to_cli_filter(enable_extra_page_navigation)
    enable_auto_suggest_bindings = to_cli_filter(enable_auto_suggest_bindings)
    registry = MergedRegistry([load_basic_bindings(), load_mouse_bindings(),
        ConditionalRegistry(load_abort_and_exit_bindings(),
        enable_abort_and_exit_bindings), ConditionalRegistry(
        load_basic_system_bindings(), enable_system_bindings),
        load_emacs_bindings(), ConditionalRegistry(
        load_emacs_open_in_editor_bindings(), enable_open_in_editor),
        ConditionalRegistry(load_emacs_search_bindings(get_search_state=
        get_search_state), enable_search), ConditionalRegistry(
        load_emacs_system_bindings(), enable_system_bindings),
        ConditionalRegistry(load_extra_emacs_page_navigation_bindings(),
        enable_extra_page_navigation), load_vi_bindings(get_search_state=
        get_search_state), ConditionalRegistry(
        load_vi_open_in_editor_bindings(), enable_open_in_editor),
        ConditionalRegistry(load_vi_search_bindings(get_search_state=
        get_search_state), enable_search), ConditionalRegistry(
        load_vi_system_bindings(), enable_system_bindings),
        ConditionalRegistry(load_extra_vi_page_navigation_bindings(),
        enable_extra_page_navigation), ConditionalRegistry(
        load_auto_suggestion_bindings(), enable_auto_suggest_bindings)])
    return registry