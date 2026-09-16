def plot_line(self, points: list, color='black', point_visibility=False):
    last_point = ()
    for point in points:
        this_point = self.plot_point(point[0], point[1], color=color,
            visible=point_visibility)
        if last_point:
            self.canvas.create_line(last_point + this_point, fill=color)
        last_point = this_point