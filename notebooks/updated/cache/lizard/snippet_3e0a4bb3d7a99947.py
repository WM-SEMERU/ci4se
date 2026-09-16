def start(self):
    for config_class in self.watched_configurables:
        monitor = ConfigFileMonitor(config_class, self.config_dir)
        self.observers.append(monitor.start(self.add_configurable, self.
            update_configurable, self.remove_configurable))
    wait_on_event(self.shutdown)