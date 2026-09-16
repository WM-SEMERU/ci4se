def stasher(self):
    stashed = [False]
    clean = [False]

    def stash():
        if clean[0] or not self.repo.is_dirty(submodules=False):
            clean[0] = True
            return
        if stashed[0]:
            return
        if self.change_count > 1:
            message = 'stashing {0} changes'
        else:
            message = 'stashing {0} change'
        print(colored(message.format(self.change_count), 'magenta'))
        try:
            self._run('stash')
        except GitError as e:
            raise StashError(stderr=e.stderr, stdout=e.stdout)
        stashed[0] = True
    yield stash
    if stashed[0]:
        print(colored('unstashing', 'magenta'))
        try:
            self._run('stash', 'pop')
        except GitError as e:
            raise UnstashError(stderr=e.stderr, stdout=e.stdout)