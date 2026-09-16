def get_commit_message(self, commit_sha):
    cmd = ['git', 'show', '-s', '--format=%B', commit_sha]
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    message = output.strip().decode('utf-8')
    if self.config['fix_commit_msg']:
        return message.replace('#', 'GH-')
    else:
        return message