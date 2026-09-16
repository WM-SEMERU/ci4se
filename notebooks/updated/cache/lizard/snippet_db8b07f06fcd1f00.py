def completion_pre_event_input_accelerators(editor, event):
    process_event = True
    if editor.completer:
        if editor.completer.popup().isVisible():
            if event.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape,
                Qt.Key_Tab, Qt.Key_Backtab):
                event.ignore()
                process_event = False
                return process_event
    if event.modifiers() in (Qt.ControlModifier, Qt.MetaModifier
        ) and event.key() == Qt.Key_Space:
        process_event = False
        if not editor.completer:
            return process_event
        perform_completion(editor)
    return process_event