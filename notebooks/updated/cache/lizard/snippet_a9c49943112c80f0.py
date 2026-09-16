def evalsha(self, sha, numkeys, *keys_and_args):
    return self.execute_command('EVALSHA', sha, numkeys, *keys_and_args)