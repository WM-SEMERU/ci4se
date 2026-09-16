def our_IsUsableForDesktopGUI(m):
    if guess_bitDepth(Q.CGDisplayModeCopyPixelEncoding(m)) != 24:
        return False
    if Q.CGDisplayModeGetWidth(m) < 640:
        return False
    if Q.CGDisplayModeGetHeight(m) < 480:
        return False
    return True