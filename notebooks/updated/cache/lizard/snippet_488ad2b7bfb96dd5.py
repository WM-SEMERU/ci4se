def stdout(self):
    stdout_path = os.path.join(self.config.artifact_dir, 'stdout')
    if not os.path.exists(stdout_path):
        raise AnsibleRunnerException('stdout missing')
    return open(os.path.join(self.config.artifact_dir, 'stdout'), 'r')