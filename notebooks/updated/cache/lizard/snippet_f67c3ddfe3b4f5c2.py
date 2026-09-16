def linkify(self, timeperiods, contacts, services, hosts):
    self.linkify_with_timeperiods(timeperiods, 'escalation_period')
    self.linkify_with_contacts(contacts)
    self.linkify_es_by_s(services)
    self.linkify_es_by_h(hosts)