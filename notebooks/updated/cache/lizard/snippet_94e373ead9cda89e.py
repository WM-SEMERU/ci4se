def is_system_defined_breakpoint(self, address):
    if address:
        module = self.get_module_at_address(address)
        if module:
            return module.match_name('ntdll') or module.match_name('kernel32')
    return False