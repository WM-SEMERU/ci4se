def get_interfaces_counters(self):
    query = junos_views.junos_iface_counter_table(self.device)
    query.get()
    interface_counters = {}
    for interface, counters in query.items():
        interface_counters[interface] = {k: (v if v is not None else -1) for
            k, v in counters}
    return interface_counters