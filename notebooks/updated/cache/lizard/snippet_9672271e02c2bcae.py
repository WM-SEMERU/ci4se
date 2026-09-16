def register_signal_handler(self, signal_name, handler_function):
    self.bus.add_signal_receiver(signal_wrapper(handler_function),
        signal_name=signal_name, dbus_interface=self.IFACE, bus_name=self.
        name, path=self.OBJ_PATH)