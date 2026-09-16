def check_valid_color(color):
    if color in list(mcolors.CSS4_COLORS.keys()) + ['#4CB391']:
        logging.info('Nanoplotter: Valid color {}.'.format(color))
        return color
    else:
        logging.info('Nanoplotter: Invalid color {}, using default.'.format
            (color))
        sys.stderr.write('Invalid color {}, using default.\n'.format(color))
        return '#4CB391'