def add(self, chassis):
    self.chassis_chain[chassis] = IxeChassis(self.session, chassis, len(
        self.chassis_chain) + 1)
    self.chassis_chain[chassis].connect()