def cmd_signing_remove(self, args):
    if not self.master.mavlink20():
        print('You must be using MAVLink2 for signing')
        return
    self.master.mav.setup_signing_send(self.target_system, self.
        target_component, [0] * 32, 0)
    self.master.disable_signing()
    print('Removed signing')