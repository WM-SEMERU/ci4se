def compose(self, *args, **kwargs):
    linebreak = kwargs.pop('linebreak', '\n')
    if len(args) > 0:
        self.args = args
    self._update(**kwargs)
    fkwargs = {}
    modtmpl = []
    for line in self:
        cline = copy(line)
        for match in self._regex.findall(line):
            search = '[{}]'.format('|'.join(match))
            name, indent, delim, qual, _ = match
            if indent != '':
                indent = ' ' * int(indent)
            delim = delim.replace('\\|', '|')
            data = getattr(self, name, None)
            if data is None:
                cline = cline.replace(search, '')
                continue
            elif delim.isdigit():
                fkwargs[name] = getattr(self, '_fmt_' + name)()
            else:
                fkwargs[name] = linebreak.join([(indent + k + delim + qual +
                    v + qual) for k, v in data.items()])
            cline = cline.replace(search, '{' + name + '}')
        modtmpl.append(cline)
    modtmpl = '\n'.join(modtmpl)
    print(modtmpl)
    dct = self.get_kwargs()
    dct.update(fkwargs)
    return self._constructor(textobj=modtmpl.format(*self.args, **dct))