def get_pretty_location(self, blank_parent_part: bool=False,
    append_file_ext: bool=True, compact_file_ext: bool=False):
    if append_file_ext:
        if compact_file_ext:
            suffix = self.ext if self.is_singlefile else ''
        else:
            suffix = ' (' + self.get_pretty_file_ext() + ')'
    else:
        suffix = ''
    if blank_parent_part:
        idx = self.location.rfind(sep)
        return ' ' * (idx - 1 - len(sep)) + '|--' + self.location[idx + 1:
            ] + suffix
    else:
        return self.location + suffix