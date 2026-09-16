def on_service_modify(self, svc_ref, old_properties):
    with self._lock:
        if self.reference is None:
            return self.on_service_arrival(svc_ref)
        else:
            best_ref = self._context.get_service_reference(self.requirement
                .specification, self.requirement.filter)
            if best_ref is self.reference:
                if svc_ref is self.reference:
                    self._ipopo_instance.update(self, self._value, svc_ref,
                        old_properties)
            else:
                self.on_service_departure(self.reference)
        return None