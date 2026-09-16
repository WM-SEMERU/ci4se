def cmd_zoom(self, args):
    if len(args) < 2:
        print('map zoom WIDTH(m)')
        return
    ground_width = float(args[1])
    self.map.set_zoom(ground_width)