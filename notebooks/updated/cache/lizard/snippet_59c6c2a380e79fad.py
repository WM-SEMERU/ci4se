def write(editor, location, force=False):
    if location and not force and os.path.exists(location):
        editor.show_message('File exists (add ! to overriwe)')
    else:
        eb = editor.window_arrangement.active_editor_buffer
        if location is None and eb.location is None:
            editor.show_message(_NO_FILE_NAME)
        else:
            eb.write(location)