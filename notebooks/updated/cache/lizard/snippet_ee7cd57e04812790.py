def guithread(function):

    def new_guithread_function(*args, **kwargs):
        if wx.Thread_IsMain():
            return function(*args, **kwargs)
        else:
            wx.CallAfter(function, *args, **kwargs)
    return new_guithread_function