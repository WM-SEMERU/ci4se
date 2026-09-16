def is_empty(self):
    return not bool(self.title or self.subtitle or self.part_number or self
        .part_name or self.non_sort or self.type)