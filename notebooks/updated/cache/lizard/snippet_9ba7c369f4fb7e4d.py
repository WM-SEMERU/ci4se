def plot_high_levels_data(self):
    high_level = self.level_box.GetValue()
    self.UPPER_LEVEL_NAME = self.level_names.GetValue()
    self.UPPER_LEVEL_MEAN = self.mean_type_box.GetValue()
    draw_net(self.high_level_eqarea)
    what_is_it = self.level_box.GetValue() + ': ' + self.level_names.GetValue()
    self.high_level_eqarea.text(-1.2, 1.15, what_is_it, {'family': self.
        font_type, 'fontsize': 10 * self.GUI_RESOLUTION, 'style': 'normal',
        'va': 'center', 'ha': 'left'})
    if self.ie_open:
        self.ie.draw_net()
        self.ie.write(what_is_it)
    self.plot_high_level_elements()
    self.plot_high_level_means()
    self.update_high_level_stats()
    if self.check_orient_on:
        self.calc_and_plot_sample_orient_check()
    self.canvas4.draw()
    if self.ie_open:
        self.ie.draw()