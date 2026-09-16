def set_user_handle_type(library, user_handle):
    global ViHndlr
    if user_handle is None:
        user_handle_p = c_void_p
    else:
        user_handle_p = POINTER(type(user_handle))
    ViHndlr = FUNCTYPE(ViStatus, ViSession, ViEventType, ViEvent, user_handle_p
        )
    library.viInstallHandler.argtypes = [ViSession, ViEventType, ViHndlr,
        user_handle_p]
    library.viUninstallHandler.argtypes = [ViSession, ViEventType, ViHndlr,
        user_handle_p]