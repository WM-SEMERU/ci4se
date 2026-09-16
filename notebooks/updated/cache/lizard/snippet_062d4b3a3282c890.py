def get_devices(self):

    def process_result(result):
        return [self.get_device(dev) for dev in result]
    return Command('get', [ROOT_DEVICES], process_result=process_result)