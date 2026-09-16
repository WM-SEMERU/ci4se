def set_tag(self, uid):
    if self.debug:
        print('Selecting UID ' + str(uid))
    if self.uid != None:
        self.deauth()
    self.uid = uid
    return self.rfid.select_tag(uid)