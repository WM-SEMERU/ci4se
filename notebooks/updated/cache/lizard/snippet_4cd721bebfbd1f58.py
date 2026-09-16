def register_account_control(self, control):
    if self.initialized:
        raise RegisterAccountControlPostInit()
    self.account_controls.append(control)