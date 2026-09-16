def find_1wf_files(self):
    regex = re.compile('out_1WF(\\d+)(\\.nc)?$')
    wf_paths = [f for f in self.list_filepaths() if regex.match(os.path.
        basename(f))]
    if not wf_paths:
        return None
    pertfile_list = []
    for path in wf_paths:
        name = os.path.basename(path)
        match = regex.match(name)
        pertcase, ncext = match.groups()
        pertfile_list.append((int(pertcase), path))
    pertfile_list = sorted(pertfile_list, key=lambda t: t[0])
    return [dict2namedtuple(pertcase=item[0], path=item[1]) for item in
        pertfile_list]