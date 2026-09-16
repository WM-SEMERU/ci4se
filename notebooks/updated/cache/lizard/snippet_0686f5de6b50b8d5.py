def generate_patches(self):
    start_pos = self.start_position or Position(None, None)
    end_pos = self.end_position or Position(None, None)
    path_list = Query._walk_directory(self.root_directory)
    path_list = Query._sublist(path_list, start_pos.path, end_pos.path)
    path_list = (path for path in path_list if Query._path_looks_like_code(
        path) and self.path_filter(path) or self.inc_extensionless and
        helpers.is_extensionless(path))
    for path in path_list:
        try:
            lines = list(open(path))
        except (IOError, UnicodeDecodeError):
            continue
        for patch in self.suggestor(lines):
            if path == start_pos.path:
                if patch.start_line_number < start_pos.line_number:
                    continue
            if path == end_pos.path:
                if patch.end_line_number >= end_pos.line_number:
                    break
            old_lines = lines[patch.start_line_number:patch.end_line_number]
            if patch.new_lines is None or patch.new_lines != old_lines:
                patch.path = path
                yield patch
                lines[:] = list(open(path))