def setup(self, artifacts, use_tsk, reason, grr_server_url, grr_username,
    grr_password, approvers=None, verify=True):
    super(GRRHuntArtifactCollector, self).setup(reason, grr_server_url,
        grr_username, grr_password, approvers=approvers, verify=verify)
    self.artifacts = [item.strip() for item in artifacts.strip().split(',')]
    if not artifacts:
        self.state.add_error('No artifacts were specified.', critical=True)
    self.use_tsk = use_tsk