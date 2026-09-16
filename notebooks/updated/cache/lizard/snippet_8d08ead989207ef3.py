def wm_preferences(name, user=None, action_double_click_titlebar=None,
    action_middle_click_titlebar=None, action_right_click_titlebar=None,
    application_based=None, audible_bell=None, auto_raise=None,
    auto_raise_delay=None, button_layout=None, disable_workarounds=None,
    focus_mode=None, focus_new_windows=None, mouse_button_modifier=None,
    num_workspaces=None, raise_on_click=None, resize_with_right_button=None,
    theme=None, titlebar_font=None, titlebar_uses_system_font=None,
    visual_bell=None, visual_bell_type=None, workspace_names=None, **kwargs):
    gnome_kwargs = {'user': user, 'schema': 'org.gnome.desktop.wm.preferences'}
    preferences = ['action_double_click_titlebar',
        'action_middle_click_titlebar', 'action_right_click_titlebar',
        'application_based', 'audible_bell', 'auto_raise',
        'auto_raise_delay', 'button_layout', 'disable_workarounds',
        'focus_mode', 'focus_new_windows', 'mouse_button_modifier',
        'num_workspaces', 'raise_on_click', 'resize_with_right_button',
        'theme', 'titlebar_font', 'titlebar_uses_system_font',
        'visual_bell', 'visual_bell_type', 'workspace_names']
    preferences_hash = {}
    for pref in preferences:
        if pref in locals() and locals()[pref] is not None:
            key = re.sub('_', '-', pref)
            preferences_hash[key] = locals()[pref]
    return _do(name, gnome_kwargs, preferences_hash)