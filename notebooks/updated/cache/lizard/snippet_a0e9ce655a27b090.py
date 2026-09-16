def auto():
    try:
        Style.enabled = False
        Style.enabled = sys.stdout.isatty()
    except (AttributeError, TypeError):
        pass