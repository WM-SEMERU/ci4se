def upload(self, cmd: str, meta: dict):
    index = os.path.join(self.cached_repo, self.INDEX_FILE)
    if os.path.exists(index):
        os.remove(index)
    self._log.info('Writing the new index.json ...')
    with open(index, 'w') as _out:
        json.dump(self.contents, _out)
    git.add(self.cached_repo, [index])
    message = self.COMMIT_MESSAGES[cmd].format(**meta)
    if self.signoff:
        global_conf_path = os.path.expanduser('~/.gitconfig')
        if os.path.exists(global_conf_path):
            with open(global_conf_path, 'br') as _in:
                conf = ConfigFile.from_file(_in)
                try:
                    name = conf.get(b'user', b'name').decode()
                    email = conf.get(b'user', b'email').decode()
                    message += self.DCO_MESSAGE.format(name=name, email=email)
                except KeyError:
                    self._log.warning(
                        'Did not find name or email in %s, committing without DCO.'
                        , global_conf_path)
        else:
            self._log.warning(
                'Global git configuration file %s does not exist, committing without DCO.'
                , global_conf_path)
    else:
        self._log.info('Committing the index without DCO.')
    git.commit(self.cached_repo, message=message)
    self._log.info('Pushing the updated index ...')
    git.push(self.cached_repo, self.remote_url, b'master')
    if self._are_local_and_remote_heads_different():
        self._log.error('Push has failed')
        raise ValueError('Push has failed')