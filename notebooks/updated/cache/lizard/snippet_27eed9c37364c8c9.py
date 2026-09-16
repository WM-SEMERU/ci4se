def plot_mv_grid_expansion_costs(self, **kwargs):
    if (self.network.pypsa is not None and self.network.results.
        grid_expansion_costs is not None):
        if isinstance(self, EDisGo):
            grid_expansion_costs = (self.network.results.
                grid_expansion_costs.reset_index())
            grid_expansion_costs['index'] = grid_expansion_costs['index'
                ].apply(lambda _: repr(_))
            grid_expansion_costs.set_index('index', inplace=True)
        else:
            grid_expansion_costs = self.network.results.grid_expansion_costs
        plots.mv_grid_topology(self.network.pypsa, self.network.config,
            line_color='expansion_costs', grid_expansion_costs=
            grid_expansion_costs, filename=kwargs.get('filename', None),
            grid_district_geom=kwargs.get('grid_district_geom', True),
            background_map=kwargs.get('background_map', True),
            limits_cb_lines=kwargs.get('limits_cb_lines', None), xlim=
            kwargs.get('xlim', None), ylim=kwargs.get('ylim', None),
            lines_cmap=kwargs.get('lines_cmap', 'inferno_r'), title=kwargs.
            get('title', ''), scaling_factor_line_width=kwargs.get(
            'scaling_factor_line_width', None))
    else:
        if self.network.pypsa is None:
            logging.warning(
                'pypsa representation of MV grid needed to plot grid expansion costs.'
                )
        if self.network.results.grid_expansion_costs is None:
            logging.warning('Grid expansion cost results needed to plot them.')