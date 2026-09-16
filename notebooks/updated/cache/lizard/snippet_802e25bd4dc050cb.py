def track_name_event(self, name):
    l = self.int_to_varbyte(len(name))
    return '\x00' + META_EVENT + TRACK_NAME + l + name