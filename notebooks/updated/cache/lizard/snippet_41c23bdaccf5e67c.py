def print_settings_example():
    SETTING_EXAMPLE_LIST = json.loads(os.getenv('SETTING_EXAMPLE_LIST', '[]'))
    SETTING_EXAMPLE_STRING = os.getenv('SETTING_EXAMPLE_STRING', 'default')
    print('List setting values: {}'.format(SETTING_EXAMPLE_LIST))
    print('String setting value: {}'.format(SETTING_EXAMPLE_STRING))