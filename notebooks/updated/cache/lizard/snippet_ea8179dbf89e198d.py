def handle_output(self, workunit, label, s):
    if os.path.exists(self._html_dir):
        path = os.path.join(self._html_dir, '{}.{}'.format(workunit.id, label))
        output_files = self._output_files[workunit.id]
        if path not in output_files:
            f = open(path, 'w')
            output_files[path] = f
        else:
            f = output_files[path]
        f.write(self._htmlify_text(s))
        f.flush()