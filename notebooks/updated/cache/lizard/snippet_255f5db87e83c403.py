def handle_reboot(self):
    self.services.stop_all()
    try:
        yield
    finally:
        self.wait_for_boot_completion()
        if self.is_rootable:
            self.root_adb()
    self.services.start_all()