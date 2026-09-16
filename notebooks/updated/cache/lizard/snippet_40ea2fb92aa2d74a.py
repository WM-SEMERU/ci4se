def fmthours(radians, norm='wrap', precision=3, seps='::'):
    return _fmtsexagesimal(radians * R2H, norm, 24, seps, precision=precision)