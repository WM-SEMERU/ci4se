def add_signal_receiver(self, callback_fn, signal, user_arg):
    if signal in self._signal_names:
        s = Signal(signal, callback_fn, user_arg)
        self._signals[signal] = s
        self._bus.add_signal_receiver(s.signal_handler, signal,
            dbus_interface=self._dbus_addr, path=self._path)
    else:
        raise BTSignalNameNotRecognisedException