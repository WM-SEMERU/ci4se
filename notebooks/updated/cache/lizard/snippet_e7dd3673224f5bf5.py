def update_controller_info(self):
    self.controller_info = customer_details(self._user_token)
    self.controller_status = status_schedule(self._user_token)
    if self.controller_info is None or self.controller_status is None:
        return False
    self.current_controller = self.controller_info['controllers'][0]
    self.status = self.current_controller['status']
    self.controller_id = self.current_controller['controller_id']
    self.customer_id = self.controller_info['customer_id']
    self.user_id = self.controller_status['user_id']
    self.num_relays = len(self.controller_status['relays'])
    self.relays = self.controller_status['relays']
    self.name = self.controller_status['name']
    self.watering_time = self.controller_status['watering_time']
    self.sensors = self.controller_status['sensors']
    try:
        self.running = self.controller_status['running']
    except KeyError:
        self.running = None
    return True