def plot_mv_line_loading(self, **kwargs):
    if (self.network.pypsa is not None and self.network.results.i_res is not
        None):
        plots.mv_grid_topology(self.network.pypsa, self.network.config,
            timestep=kwargs.get('timestep', None), line_color='loading',
            node_color=kwargs.get('node_color', None), line_load=self.
            network.results.s_res(), filename=kwargs.get('filename', None),
            arrows=kwargs.get('arrows', None), grid_district_geom=kwargs.
            get('grid_district_geom', True), background_map=kwargs.get(
            'background_map', True), voltage=self.network.results.v_res(),
            limits_cb_lines=kwargs.get('limits_cb_lines', None),
            limits_cb_nodes=kwargs.get('limits_cb_nodes', None), xlim=
            kwargs.get('xlim', None), ylim=kwargs.get('ylim', None),
            lines_cmap=kwargs.get('lines_cmap', 'inferno_r'), title=kwargs.
            get('title', ''), scaling_factor_line_width=kwargs.get(
            'scaling_factor_line_width', None))
    else:
        if self.network.pypsa is None:
            logging.warning(
                'pypsa representation of MV grid needed to plot line loading.')
        if self.network.results.i_res is None:
            logging.warning(
                'Currents `i_res` from power flow analysis must be available to plot line loading.'
                )