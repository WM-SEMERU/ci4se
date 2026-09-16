def cmd_fft(args):
    from MAVProxy.modules.lib import mav_fft
    if len(args) > 0:
        condition = args[0]
    else:
        condition = None
    child = multiproc.Process(target=mav_fft.mavfft_display, args=[mestate.
        filename, condition])
    child.start()