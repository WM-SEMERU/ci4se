def new_config_event(self):
    try:
        self.on_set_config()
    except Exception as ex:
        self.logger.exception(ex)
        raise StopIteration()