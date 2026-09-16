def sorted_args(self):
    return sorted(self.args, key=lambda x: x.is_flag or x.can_be_inferred)