def get_user_modified_lines(self):
    output = {}
    FILE_NAME_RE = '^\\+\\+\\+ (.+)$'
    CHANGED_LINES_RE = '^@@ -[0-9,]+ \\+([0-9]+)(?:,([0-9]+))? @@'
    current_file_name = None
    for line in self.git_wrapper.get_min_diff(self.remote_sha1, self.local_sha1
        ).split('\n'):
        file_name_match = re.match(FILE_NAME_RE, line)
        if file_name_match:
            current_file_name, = file_name_match.groups()
            output[current_file_name] = []
            continue
        line_number_match = re.match(CHANGED_LINES_RE, line)
        if line_number_match:
            assert current_file_name
            if current_file_name == '/dev/null':
                continue
            line_start, diff_len = line_number_match.groups()
            line_start, diff_len = int(line_start), int(diff_len or 0)
            output[current_file_name].append(LinesRange(line_start, 
                line_start + diff_len))
            continue
    return output