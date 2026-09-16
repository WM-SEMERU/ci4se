def clean_pieces(self, pieces):
    ret = []
    count = 0
    for i in pieces:
        if i == '\n':
            count = count + 1
        else:
            if i == '";':
                if count:
                    ret.append('\n')
            elif count > 2:
                ret.append('\n\n')
            elif count:
                ret.append('\n' * count)
            count = 0
            ret.append(i)
    _data = ''.join(ret)
    ret = []
    for i in _data.split('\n\n'):
        if i == 'Parameters:':
            ret.extend(['Parameters:\n-----------', '\n\n'])
        elif i.find('// File:') > -1:
            ret.extend([i, '\n'])
        else:
            _tmp = textwrap.fill(i.strip())
            _tmp = self.lead_spc.sub('\\1"\\2', _tmp)
            ret.extend([_tmp, '\n\n'])
    return ret