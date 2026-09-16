def get_cmd_tuple_list(self):
    pat = re.compile('\\$\\((.+)\\)')
    argpat = re.compile('\\d+')
    options = self.job().get_opts()
    macros = self.get_opts()
    cmd_list = []
    for k in options:
        val = options[k]
        m = pat.match(val)
        if m:
            key = m.group(1)
            value = macros[key]
            cmd_list.append(('--%s' % k, str(value)))
        else:
            cmd_list.append(('--%s' % k, str(val)))
    options = self.job().get_short_opts()
    for k in options:
        val = options[k]
        m = pat.match(val)
        if m:
            key = m.group(1)
            value = macros[key]
            cmd_list.append(('-%s' % k, str(value)))
        else:
            cmd_list.append(('-%s' % k, str(val)))
    args = self.job().get_args()
    macros = self.get_args()
    for a in args:
        m = pat.match(a)
        if m:
            arg_index = int(argpat.findall(a)[0])
            try:
                cmd_list.append(('%s' % macros[arg_index], ''))
            except IndexError:
                cmd_list.append('')
        else:
            cmd_list.append(('%s' % a, ''))
    return cmd_list