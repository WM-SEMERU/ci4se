def get_default_config_help(self):
    config_help = super(PassengerCollector, self).get_default_config_help()
    config_help.update({'bin': 'The path to the binary', 'use_sudo':
        'Use sudo?', 'sudo_cmd': 'Path to sudo', 'passenger_status_bin':
        'The path to the binary passenger-status',
        'passenger_memory_stats_bin':
        'The path to the binary passenger-memory-stats'})
    return config_help