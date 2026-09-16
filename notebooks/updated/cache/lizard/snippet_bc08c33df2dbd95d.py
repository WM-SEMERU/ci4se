def file_delete(filename, settings):
    if len(settings) != 1:
        raise ValueError("Settings must only contain one item with key 'mode'."
            )
    for k, v in settings.items():
        if k == 'mode' and v == 'actual':
            try:
                os.remove(filename)
            except OSError:
                pass
        elif k == 'mode' and v == 'simulated':
            print('Simulated removal of {}'.format(filename))