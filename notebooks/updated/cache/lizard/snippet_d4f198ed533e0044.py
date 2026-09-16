def _get_reference(self):
    super()._get_reference()
    self.cube_body_id = self.sim.model.body_name2id('pot')
    self.handle_1_site_id = self.sim.model.site_name2id('pot_handle_1')
    self.handle_2_site_id = self.sim.model.site_name2id('pot_handle_2')
    self.table_top_id = self.sim.model.site_name2id('table_top')
    self.pot_center_id = self.sim.model.site_name2id('pot_center')