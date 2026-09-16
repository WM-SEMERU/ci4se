def _decode(self):
    result = []
    idx = 0
    s = self._encoded_value
    embedded = False
    errmsg = []
    errmsg.append("Invalid character '")
    while idx < len(s):
        c = s[idx]
        errmsg.append(c)
        errmsg.append("'")
        errmsg_str = ''.join(errmsg)
        if CPEComponentSimple._is_alphanum(c):
            result.append(c)
            idx += 1
            embedded = True
            continue
        if c == '\\':
            result.append(s[idx:idx + 2])
            idx += 2
            embedded = True
            continue
        if c == CPEComponent2_3_FS.WILDCARD_MULTI:
            if idx == 0 or idx == len(s) - 1:
                result.append(c)
                idx += 1
                embedded = True
                continue
            else:
                raise ValueError(errmsg_str)
        if c == CPEComponent2_3_FS.WILDCARD_ONE:
            if (idx == 0 or idx == len(s) - 1) or not embedded and s[idx - 1
                ] == CPEComponent2_3_FS.WILDCARD_ONE or embedded and s[idx + 1
                ] == CPEComponent2_3_FS.WILDCARD_ONE:
                result.append(c)
                idx += 1
                embedded = False
                continue
            else:
                raise ValueError(errmsg_str)
        result.append('\\')
        result.append(c)
        idx += 1
        embedded = True
    self._standard_value = ''.join(result)