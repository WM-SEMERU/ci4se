def make_onmousewheel_cb(widget, orient, factor=1):
    _os = platform.system()
    view_command = getattr(widget, orient + 'view')
    if _os in ('Linux', 'OpenBSD', 'FreeBSD'):

        def on_mousewheel(event):
            if event.num == 4:
                view_command('scroll', -1 * factor, 'units')
            elif event.num == 5:
                view_command('scroll', factor, 'units')
    elif _os == 'Windows':

        def on_mousewheel(event):
            view_command('scroll', -1 * int(event.delta / 120 * factor),
                'units')
    elif _os == 'Darwin':

        def on_mousewheel(event):
            view_command('scroll', event.delta, 'units')
    else:

        def on_mousewheel(event):
            pass
    return on_mousewheel