def animation(device, from_y, to_y):
    hourstime = datetime.now().strftime('%H')
    mintime = datetime.now().strftime('%M')
    current_y = from_y
    while current_y != to_y:
        with canvas(device) as draw:
            text(draw, (0, current_y), hourstime, fill='white', font=
                proportional(CP437_FONT))
            text(draw, (15, current_y), ':', fill='white', font=
                proportional(TINY_FONT))
            text(draw, (17, current_y), mintime, fill='white', font=
                proportional(CP437_FONT))
        time.sleep(0.1)
        current_y += 1 if to_y > from_y else -1