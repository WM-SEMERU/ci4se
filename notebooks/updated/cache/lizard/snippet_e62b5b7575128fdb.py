def _scrub_generated_timestamps(self, target_workdir):
    for root, _, filenames in safe_walk(target_workdir):
        for filename in filenames:
            source = os.path.join(root, filename)
            with open(source, 'r') as f:
                lines = f.readlines()
            if len(lines) < 1:
                return
            with open(source, 'w') as f:
                if not self._COMMENT_WITH_TIMESTAMP_RE.match(lines[0]):
                    f.write(lines[0])
                for line in lines[1:]:
                    f.write(line)