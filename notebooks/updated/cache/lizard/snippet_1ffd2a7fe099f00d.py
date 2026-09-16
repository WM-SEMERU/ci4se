def is_valid_for(self, entry_point, protocol):
    return self.available_for_entry_point(entry_point
        ) and self.available_for_protocol(protocol)