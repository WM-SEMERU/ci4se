def service_changed(self, event):
    kind = event.get_kind()
    reference = event.get_service_reference()
    if kind in (pelix.ServiceEvent.REGISTERED, pelix.ServiceEvent.MODIFIED):
        self.set_shell(reference)
    else:
        with self._lock:
            self.clear_shell()
            self.search_shell()