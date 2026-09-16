def _get_reference(self):
    super()._get_reference()
    self.hole_body_id = self.sim.model.body_name2id('hole')
    self.cyl_body_id = self.sim.model.body_name2id('cylinder')