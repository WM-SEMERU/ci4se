def set_window_focus_callback(window, cbfun):
    window_addr = ctypes.cast(ctypes.pointer(window), ctypes.POINTER(ctypes
        .c_long)).contents.value
    if window_addr in _window_focus_callback_repository:
        previous_callback = _window_focus_callback_repository[window_addr]
    else:
        previous_callback = None
    if cbfun is None:
        cbfun = 0
    c_cbfun = _GLFWwindowfocusfun(cbfun)
    _window_focus_callback_repository[window_addr] = cbfun, c_cbfun
    cbfun = c_cbfun
    _glfw.glfwSetWindowFocusCallback(window, cbfun)
    if previous_callback is not None and previous_callback[0] != 0:
        return previous_callback[0]