def _extract_groupstyle_docs_params(self):
    data = '\n'.join([d.rstrip().replace(self.docs['out']['spaces'], '', 1) for
        d in self.docs['in']['raw'].splitlines()])
    idx = self.dst.get_group_key_line(data, 'param')
    if idx >= 0:
        data = data.splitlines()[idx + 1:]
        end = self.dst.get_group_line('\n'.join(data))
        end = end if end != -1 else len(data)
        for i in range(end):
            line = data[i]
            param = None
            desc = ''
            ptype = ''
            m = re.match('^\\W*(\\w+)[\\W\\s]+(\\w[\\s\\w]+)', line.strip())
            if m:
                param = m.group(1).strip()
                desc = m.group(2).strip()
            else:
                m = re.match('^\\W*(\\w+)\\W*', line.strip())
                if m:
                    param = m.group(1).strip()
            if param:
                self.docs['in']['params'].append((param, desc, ptype))