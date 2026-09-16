def device_info(self):
    info = {'serial': self.serial, 'model': self.model, 'build_info': self.
        build_info, 'user_added_info': self._user_added_device_info}
    return info