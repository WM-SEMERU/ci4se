def _get_temp(self, content):
    temp = None
    for line in content.splitlines():
        if not temp:
            match = TEMP_NEEDLE.match(line)
            if match:
                temp = match.group(1).strip()
                continue
        else:
            match = TEMP_END_NEEDLE.match(line)
            if match:
                return temp
    raise IndexError(self.path)