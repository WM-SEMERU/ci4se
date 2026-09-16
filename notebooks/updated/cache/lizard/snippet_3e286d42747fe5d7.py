def get_short_history(self, ticket_id):
    msg = self.__request('ticket/{}/history'.format(str(ticket_id)))
    items = []
    lines = msg.split('\n')
    multiline_buffer = ''
    in_multiline = False
    if self.__get_status_code(lines[0]) == 200:
        if len(lines) > 2 and self.RE_PATTERNS['does_not_exist_pattern'].match(
            lines[2]):
            return None
        if len(lines) >= 4:
            for line in lines[4:]:
                if line == '':
                    if not in_multiline:
                        in_multiline = True
                    else:
                        line = multiline_buffer
                        multiline_buffer = ''
                        in_multiline = False
                elif in_multiline:
                    multiline_buffer += line
                    line = ''
                if ': ' in line:
                    hist_id, desc = line.split(': ', 1)
                    items.append((int(hist_id), desc))
    return items