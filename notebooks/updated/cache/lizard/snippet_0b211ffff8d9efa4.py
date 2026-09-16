def parse(self, parsable):
    calc, error = None, None
    try:
        f = open(parsable, 'rb')
        if is_binary_string(f.read(2048)):
            yield None, 'was read (binary data)...'
            return
        f.close()
    except IOError:
        yield None, 'read error!'
        return
    f = open(parsable, 'r', errors='surrogateescape') if six.PY3 else open(
        parsable, 'r')
    f.seek(0)
    counter, detected = 0, False
    while not detected:
        if counter > 700:
            break
        fingerprint = f.readline()
        if not fingerprint:
            break
        for name, Parser in self.Parsers.items():
            if Parser.fingerprints(fingerprint):
                for calc, error in self._parse(parsable, name):
                    detected = True
                    if not error and calc:
                        if not len(calc.structures) or not len(calc.
                            structures[-1]):
                            error = 'Valid structure is not present!'
                        if calc.info['finished'] == 1:
                            calc.warning(
                                'This calculation is not correctly finished!')
                        if not calc.info['H']:
                            error = 'XC potential is not present!'
                    yield calc, error
                if detected:
                    break
        counter += 1
    f.close()
    if not detected:
        yield None, 'was read...'