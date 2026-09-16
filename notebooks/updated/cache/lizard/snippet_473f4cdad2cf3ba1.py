def connect_after(self, slot, *extra_args):
    slot = Slot(slot, *extra_args)
    self._after_functions.add(slot)