def pyspread(S=None):
    app = MainApplication(S=S, redirect=False)
    app.MainLoop()