def _process_rules(self, rules: dict, system: System):
    self._source = None
    if not self._shall_proceed(rules):
        return
    self.context.update(rules.get('context', {}))
    self.path = rules.get('path', '')
    self.source = rules.get('source', None)
    self._process_rule(rules.get('system', None), {'system': system})
    for module in system.modules:
        self._process_rule(rules.get('module', None), {'module': module})
        for interface in module.interfaces:
            self._process_rule(rules.get('interface', None), {'interface':
                interface})
        for struct in module.structs:
            self._process_rule(rules.get('struct', None), {'struct': struct})
        for enum in module.enums:
            self._process_rule(rules.get('enum', None), {'enum': enum})