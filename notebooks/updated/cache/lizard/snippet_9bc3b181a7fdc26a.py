def render(self):
    self.symbols = set()
    go_again = True
    while go_again:
        go_again = False
        template_symbols = set(re.findall(SYMBOL_PATTERN, self.template))
        self.symbols.update(template_symbols)
        for symbol in template_symbols:
            resolved_symbol = None
            if symbol[:4] == 'aws:' and EFTemplateResolver.__AWSR:
                resolved_symbol = EFTemplateResolver.__AWSR.lookup(symbol[4:])
            elif symbol[:12] == 'credentials:':
                pass
            elif symbol[:9] == 'efconfig:':
                resolved_symbol = EFTemplateResolver.__EFCR.lookup(symbol[9:])
            elif symbol[:8] == 'version:':
                resolved_symbol = EFTemplateResolver.__VR.lookup(symbol[8:])
                if not resolved_symbol:
                    print(
                        "WARNING: Lookup failed for {{%s}} - placeholder value of 'NONE' used in rendered template"
                         % symbol)
                    resolved_symbol = 'NONE'
            else:
                if symbol in self.resolved:
                    resolved_symbol = self.resolved[symbol]
                if not resolved_symbol:
                    resolved_symbol = self.search_parameters(symbol)
            if resolved_symbol is not None:
                if isinstance(resolved_symbol, list):
                    self.template = self.template.replace('{{' + symbol +
                        '}}', '\n'.join(resolved_symbol))
                else:
                    self.template = self.template.replace('{{' + symbol +
                        '}}', resolved_symbol)
                go_again = True
    return self.template