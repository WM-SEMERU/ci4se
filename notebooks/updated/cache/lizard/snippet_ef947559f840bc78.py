def state(self):
    return Emitter(weakref.proxy(self.lib), self.lib.jit_new_state())