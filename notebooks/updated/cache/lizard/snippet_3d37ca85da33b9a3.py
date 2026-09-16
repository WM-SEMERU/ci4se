def close_websockets(self):
    self.log.info('Websocket Teardown called')
    for key in list(self.soclist.keys()):
        if self.soclist[key]:
            self.soclist[key].close()
        self.soclist.pop(key)