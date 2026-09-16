def animate(canvas, fn, delay=1.0 / 24, *args, **kwargs):
    if not IS_PY3:
        import locale
        locale.setlocale(locale.LC_ALL, '')

    def animation(stdscr):
        for frame in fn(*args, **kwargs):
            for x, y in frame:
                canvas.set(x, y)
            f = canvas.frame()
            stdscr.addstr(0, 0, '{0}\n'.format(f))
            stdscr.refresh()
            if delay:
                sleep(delay)
            canvas.clear()
    curses.wrapper(animation)