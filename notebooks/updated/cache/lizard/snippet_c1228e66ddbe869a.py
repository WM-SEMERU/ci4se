def _set_axis_position(self, axes, axis, option):
    positions = {'x': ['bottom', 'top'], 'y': ['left', 'right']}[axis]
    axis = axes.xaxis if axis == 'x' else axes.yaxis
    if option in [None, False]:
        axis.set_visible(False)
        for pos in positions:
            axes.spines[pos].set_visible(False)
    else:
        if option is True:
            option = positions[0]
        if 'bare' in option:
            axis.set_ticklabels([])
            axis.set_label_text('')
        if option != 'bare':
            option = option.split('-')[0]
            axis.set_ticks_position(option)
            axis.set_label_position(option)
    if (not self.overlaid and not self.show_frame and self.projection !=
        'polar'):
        pos = positions[1] if option and (option == 'bare' or positions[0] in
            option) else positions[0]
        axes.spines[pos].set_visible(False)