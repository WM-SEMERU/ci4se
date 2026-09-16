def scan_diff(self, diff, baseline_filename='', last_commit_hash='',
    repo_name=''):
    from unidiff import PatchSet
    from unidiff.errors import UnidiffParseError
    try:
        patch_set = PatchSet.from_string(diff)
    except UnidiffParseError:
        alert = {'alert': 'UnidiffParseError', 'hash': last_commit_hash,
            'repo_name': repo_name}
        log.error(alert)
        raise
    if self.exclude_files:
        regex = re.compile(self.exclude_files, re.IGNORECASE)
    for patch_file in patch_set:
        filename = patch_file.path
        if self.exclude_files and regex.search(filename):
            continue
        if filename == baseline_filename:
            continue
        for results, plugin in self._results_accumulator(filename):
            results.update(self._extract_secrets_from_patch(patch_file,
                plugin, filename))