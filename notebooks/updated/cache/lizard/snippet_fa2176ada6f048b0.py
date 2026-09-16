def p_throttling(p):
    throttling = NoThrottlingSettings()
    if len(p) == 7:
        throttling = TailDropSettings(int(p[5]))
    p[0] = {'throttling': throttling}