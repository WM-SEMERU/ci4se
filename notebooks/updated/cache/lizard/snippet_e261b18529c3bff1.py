def _get_slots(self, empty_uid=False):
    slots = list()
    for uid, position in self.uids_strpositions.items():
        if empty_uid and not uid.startswith('empty-'):
            continue
        elif not empty_uid and uid.startswith('empty-'):
            continue
        tokens = position.split(':')
        slots.append(to_int(tokens[0]))
    return sorted(list(set(slots)))