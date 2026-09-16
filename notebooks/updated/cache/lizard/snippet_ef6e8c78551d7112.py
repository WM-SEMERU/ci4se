def start_charge(self):
    if not self.__charger_state:
        data = self._controller.command(self._id, 'charge_start',
            wake_if_asleep=True)
        if data and data['response']['result']:
            self.__charger_state = True
        self.__manual_update_time = time.time()