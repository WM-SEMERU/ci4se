def close(self):
    assert self.closed is False
    log.debug('closing interface')
    self.closed = True
    self.read_sem.release()
    self.thread.join()
    assert self.rcv_data[-1] is None
    self.rcv_data = []
    usb.util.release_interface(self.dev, self.intf_number)
    if self.kernel_driver_was_attached:
        try:
            self.dev.attach_kernel_driver(self.intf_number)
        except Exception as exception:
            log.warning('Exception attaching kernel driver: %s', str(exception)
                )
    usb.util.dispose_resources(self.dev)
    self.ep_out = None
    self.ep_in = None
    self.dev = None
    self.intf_number = None
    self.kernel_driver_was_attached = False
    self.thread = None