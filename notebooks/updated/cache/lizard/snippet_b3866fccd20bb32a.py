def reflash_firmware(self, hardware_id, ipmi=True, raid_controller=True,
    bios=True):
    return self.hardware.createFirmwareReflashTransaction(bool(ipmi), bool(
        raid_controller), bool(bios), id=hardware_id)