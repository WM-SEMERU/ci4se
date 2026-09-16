def get_word_app():
    if not has_word():
        return None
    pythoncom.CoInitialize()
    import win32com.client
    app = win32com.client.gencache.EnsureDispatch('Word.Application')
    app.Visible = False
    return app