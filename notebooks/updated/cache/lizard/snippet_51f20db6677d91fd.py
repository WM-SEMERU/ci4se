def update(self):
    self._controller.update(self._id, wake_if_asleep=False)
    data = self._controller.get_climate_params(self._id)
    if data:
        if time.time() - self.__manual_update_time > 60:
            self.__is_auto_conditioning_on = data['is_auto_conditioning_on']
            self.__is_climate_on = data['is_climate_on']
            self.__driver_temp_setting = data['driver_temp_setting'] if data[
                'driver_temp_setting'] else self.__driver_temp_setting
            self.__passenger_temp_setting = data['passenger_temp_setting'
                ] if data['passenger_temp_setting'
                ] else self.__passenger_temp_setting
        self.__inside_temp = data['inside_temp'] if data['inside_temp'
            ] else self.__inside_temp
        self.__outside_temp = data['outside_temp'] if data['outside_temp'
            ] else self.__outside_temp
        self.__fan_status = data['fan_status']