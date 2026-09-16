def stalk_variable(self, tid, address, size, action=None):
    bp = self.__set_variable_watch(tid, address, size, action)
    if not bp.is_one_shot():
        self.enable_one_shot_hardware_breakpoint(tid, address)