def run_loop(leds=all_leds):
    print('Loop started.\nPress Ctrl+C to break out of the loop.')
    while 1:
        try:
            if switch():
                [led.on() for led in leds]
            else:
                [led.off() for led in leds]
        except OSError:
            break