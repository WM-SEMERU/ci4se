def set_collapsed(block, val):
    if block is None:
        return
    state = block.userState()
    if state == -1:
        state = 0
    state &= 2013265919
    state |= int(val) << 27
    block.setUserState(state)