def do_list(self, line):
    repo_names = self.network.repo_names
    print('Known repos:')
    print('    ' + '\n    '.join(repo_names))