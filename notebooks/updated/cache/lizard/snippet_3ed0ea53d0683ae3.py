def _add_job_control_plane(self):
    if not self._has_jcp:
        jcp = self.graph.addOperator(kind='spl.control::JobControlPlane',
            name='JobControlPlane')
        jcp.viewable = False
        self._has_jcp = True