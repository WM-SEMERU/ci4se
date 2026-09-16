def this_boot(self, bootid=None):
    if bootid is None:
        bootid = _id128.get_boot().hex
    else:
        bootid = getattr(bootid, 'hex', bootid)
    self.add_match(_BOOT_ID=bootid)