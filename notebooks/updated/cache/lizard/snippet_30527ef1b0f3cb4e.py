def _apply_dict(self, qe_dict):
    for k, v in qe_dict.items():
        k = resolve_name(self.type, k)
        if not k in self.__query:
            self.__query[k] = v
            continue
        if not isinstance(self.__query[k], dict) or not isinstance(v, dict):
            raise BadQueryException(
                'Multiple assignments to a field must all be dicts.')
        self.__query[k].update(**v)