def pretty_print(self, as_list=False, show_datetime=True):
    ppl = [entry.pretty_print(show_datetime) for entry in self.entries]
    if as_list:
        return ppl
    return '\n'.join(ppl)