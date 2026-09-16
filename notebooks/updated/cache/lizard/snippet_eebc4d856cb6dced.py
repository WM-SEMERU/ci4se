def matches_pattern(self, other):
    properties = self._message_properties()
    ismatch = False
    if isinstance(other, Message) and self.code == other.code:
        for prop in properties:
            for key, prop_val in prop.items():
                if hasattr(other, key):
                    key_val = getattr(other, key)
                    ismatch = self._test_match(prop_val, key_val)
                else:
                    ismatch = False
                if not ismatch:
                    break
            if not ismatch:
                break
    return ismatch