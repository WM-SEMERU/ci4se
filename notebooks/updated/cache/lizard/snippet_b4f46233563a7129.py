def save_settings(self):

    def _save_displayed_setting(conf, submenu):
        for source, visible_sensors in self.view.graphs_menu.active_sensors.items(
            ):
            section = source + ',' + submenu
            conf.add_section(section)
            sources = self.sources
            logging.debug('Saving settings for %s', source)
            logging.debug('Visible sensors %s', visible_sensors)
            curr_sensor = [x for x in sources if x.get_source_name() == source
                ][0]
            sensor_list = curr_sensor.get_sensor_list()
            for sensor_id, sensor in enumerate(sensor_list):
                try:
                    conf.set(section, sensor, str(visible_sensors[sensor_id]))
                except IndexError:
                    conf.set(section, sensor, str(True))
    if not user_config_dir_exists():
        make_user_config_dir()
    conf = configparser.ConfigParser()
    config_file = get_user_config_file()
    with open(config_file, 'w') as cfgfile:
        conf.add_section('GraphControll')
        conf.set('GraphControll', 'refresh', str(self.refresh_rate))
        conf.set('GraphControll', 'UTF8', str(self.smooth_graph_mode))
        if self.temp_thresh:
            conf.set('GraphControll', 'TTHRESH', str(self.temp_thresh))
        _save_displayed_setting(conf, 'Graphs')
        _save_displayed_setting(conf, 'Summaries')
        conf.write(cfgfile)