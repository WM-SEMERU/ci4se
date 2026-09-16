def _get_desktop_size():
    if platform.system() == 'Linux':
        try:
            xrandr_query = subprocess.check_output(['xrandr', '--query'])
            sizes = re.findall('\\bconnected primary (\\d+)x(\\d+)', str(
                xrandr_query))
            if sizes[0]:
                return point.Point(int(sizes[0][0]), int(sizes[0][1]))
        except:
            logging.error('Failed to get the resolution from xrandr.')
    display_info = pygame.display.Info()
    return point.Point(display_info.current_w, display_info.current_h)