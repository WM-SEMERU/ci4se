def plot(self, figure_list):
    if not self.data == {} and self.data['image_data'] is None:
        axes = figure_list[0].axes[0]
        if len(axes.images) > 0:
            self.data['image_data'] = np.array(axes.images[0].get_array())
            self.data['extent'] = np.array(axes.images[0].get_extent())
            self.plot_settings['cmap'] = axes.images[0].get_cmap().name
            self.plot_settings['xlabel'] = axes.get_xlabel()
            self.plot_settings['ylabel'] = axes.get_ylabel()
            self.plot_settings['title'] = axes.get_title()
            self.plot_settings['interpol'] = axes.images[0].get_interpolation()
    Script.plot(self, figure_list)