def update_gen_report(self, role, file, original):
    state = self.report['state']
    if not os.path.exists(self.paths[file]):
        state['ok_role'] += 1
        self.report['roles'][role]['state'] = 'ok'
    elif self.report['roles'][role][file] != original and self.report['roles'][
        role]['state'] != 'ok':
        state['changed_role'] += 1
        self.report['roles'][role]['state'] = 'changed'
    elif self.report['roles'][role][file] == original:
        state['skipped_role'] += 1
        self.report['roles'][role]['state'] = 'skipped'
        return
    utils.string_to_file(self.paths[file], original)