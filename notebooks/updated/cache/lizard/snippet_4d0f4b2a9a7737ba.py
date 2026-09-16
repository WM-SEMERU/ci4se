def any_status_is(weather_list, status, weather_code_registry):
    for weather in weather_list:
        if status_is(weather, status, weather_code_registry):
            return True
    return False