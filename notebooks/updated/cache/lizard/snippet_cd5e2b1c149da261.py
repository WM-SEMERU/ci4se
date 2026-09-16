def guess_payload_class(self, payload):
    for t in self.aliastypes:
        for fval, cls in t.payload_guess:
            if all(hasattr(self, k) and v == self.getfieldval(k) for k, v in
                six.iteritems(fval)):
                return cls
    return self.default_payload_class(payload)