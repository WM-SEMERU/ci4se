def stop_charge(self):
    if self.__charger_state:
        data = self._controller.command(self._id, 'charge_stop',
            wake_if_asleep=True)
        if data and data['response']['result']:
            self.__charger_state = False
        self.__manual_update_time = time.time()