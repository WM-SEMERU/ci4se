def launch_browser(attempt_launch_browser=True):
    _DISPLAY_VARIABLES = ['DISPLAY', 'WAYLAND_DISPLAY', 'MIR_SOCKET']
    _WEBBROWSER_NAMES_BLACKLIST = ['www-browser', 'lynx', 'links', 'elinks',
        'w3m']
    import webbrowser
    launch_browser = attempt_launch_browser
    if launch_browser:
        if 'linux' in sys.platform and not any(os.getenv(var) for var in
            _DISPLAY_VARIABLES):
            launch_browser = False
        try:
            browser = webbrowser.get()
            if hasattr(browser, 'name'
                ) and browser.name in _WEBBROWSER_NAMES_BLACKLIST:
                launch_browser = False
        except webbrowser.Error:
            launch_browser = False
    return launch_browser