def unhook_symbol(self, symbol_name):
    sym = self.loader.find_symbol(symbol_name)
    if sym is None:
        l.warning('Could not find symbol %s', symbol_name)
        return False
    if sym.owner is self.loader._extern_object:
        l.warning(
            'Refusing to unhook external symbol %s, replace it with another hook if you want to change it'
            , symbol_name)
        return False
    hook_addr, _ = self.simos.prepare_function_symbol(symbol_name,
        basic_addr=sym.rebased_addr)
    self.unhook(hook_addr)
    return True