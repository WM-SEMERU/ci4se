def toggle_autojump():
    if not autojump_enabled():
        with open(AUTOJUMP_FILE, 'w+') as ajfile:
            ajfile.write('enabled')
    else:
        os.remove(AUTOJUMP_FILE)