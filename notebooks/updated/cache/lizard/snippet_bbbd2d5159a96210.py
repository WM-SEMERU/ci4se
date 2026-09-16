def cmd_status_codes_counter(self):
    status_codes = defaultdict(int)
    for line in self._valid_lines:
        status_codes[line.status_code] += 1
    return status_codes