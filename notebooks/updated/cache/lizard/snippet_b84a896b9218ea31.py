def _chk_docopt_kws(self, docdict, exp):
    for key, val in docdict.items():
        if isinstance(val, str):
            assert '=' not in val, self._err("'=' FOUND IN VALUE", key, val,
                exp)
        elif key != 'help' and key not in self.exp_keys and key not in self.exp_elems:
            raise RuntimeError(self._err('UNKNOWN KEY', key, val, exp))