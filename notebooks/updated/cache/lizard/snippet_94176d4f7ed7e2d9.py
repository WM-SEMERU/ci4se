def attinq(self, attribute=None):
    position = self._first_adr
    if isinstance(attribute, str):
        for _ in range(0, self._num_att):
            name, next_adr = self._read_adr_fast(position)
            if name.strip().lower() == attribute.strip().lower():
                return self._read_adr(position)
            position = next_adr
        raise KeyError('No attribute {}'.format(attribute))
    elif isinstance(attribute, int):
        if attribute < 0 or attribute > self._num_zvariable:
            raise KeyError('No attribute {}'.format(attribute))
        for _ in range(0, attribute):
            name, next_adr = self._read_adr_fast(position)
            position = next_adr
        return self._read_adr(position)
    else:
        print('Please set attribute keyword equal to the name or ',
            'number of an attribute')
        attrs = self._get_attnames()
        print(attrs)
        for x in range(0, self._num_att):
            name = list(attrs[x].keys())[0]
            print('NAME: ' + name + ', NUMBER: ' + str(x) + ', SCOPE: ' +
                attrs[x][name])
        return attrs