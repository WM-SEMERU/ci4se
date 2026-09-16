def _GetFrameCodeObjectName(frame):
    if frame.f_code.co_argcount >= 1 and 'self' == frame.f_code.co_varnames[0]:
        return frame.f_locals['self'
            ].__class__.__name__ + '.' + frame.f_code.co_name
    else:
        return frame.f_code.co_name