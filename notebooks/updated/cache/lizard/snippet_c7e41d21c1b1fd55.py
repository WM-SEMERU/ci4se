def update_redirect(self):
    if self.last_child:
        self._resolved_pid.redirect(self.last_child)
    elif any(map(lambda pid: pid.status not in [PIDStatus.DELETED,
        PIDStatus.REGISTERED, PIDStatus.RESERVED], super(PIDNodeVersioning,
        self).children.all())):
        raise PIDRelationConsistencyError(
            'Invalid relation state. Only REGISTERED, RESERVED and DELETED PIDs are supported.'
            )