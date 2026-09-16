def _draw_background(self, divisions=10):
    self.canvas.create_arc(2, 2, self.size - 2, self.size - 2, style=tk.
        PIESLICE, start=-60, extent=30, fill='red')
    self.canvas.create_arc(2, 2, self.size - 2, self.size - 2, style=tk.
        PIESLICE, start=-30, extent=60, fill='yellow')
    self.canvas.create_arc(2, 2, self.size - 2, self.size - 2, style=tk.
        PIESLICE, start=30, extent=210, fill='green')
    inner_tick_radius = int(self.size * 0.4)
    outer_tick_radius = int(self.size * 0.5)
    for tick in range(divisions):
        angle_in_radians = 2.0 * cmath.pi / 3.0 + tick / divisions * (5.0 *
            cmath.pi / 3.0)
        inner_point = cmath.rect(inner_tick_radius, angle_in_radians)
        outer_point = cmath.rect(outer_tick_radius, angle_in_radians)
        self.canvas.create_line(*self.to_absolute(inner_point.real,
            inner_point.imag), *self.to_absolute(outer_point.real,
            outer_point.imag), width=1)