def _compute_am_i_owner(self):
    for rec in self:
        rec.am_i_owner = rec.create_uid == self.env.user