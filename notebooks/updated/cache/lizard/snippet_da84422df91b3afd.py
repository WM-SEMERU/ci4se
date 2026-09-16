def set_rgb_points(self, rgb_points, *args):
    if not args:
        self.rgb_points = rgb_points
    elif len(args) == 2:
        self.rgb_points = rgb_points, args[0], args[1]
    elif len(args) == 5:
        self.rgb_points = (rgb_points, args[0]), (args[1], args[2]), (args[
            3], args[4])