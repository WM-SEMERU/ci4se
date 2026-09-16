def cron_ddmrp_adu(self, automatic=False):
    self.env['ddmrp.adjustment.demand'].search([]).unlink()
    super().cron_ddmrp_adu(automatic)
    today = fields.Date.today()
    for op in self.search([]).filtered('extra_demand_ids'):
        to_add = sum(op.extra_demand_ids.filtered(lambda r: r.date_start <=
            today <= r.date_end).mapped('extra_demand'))
        if to_add:
            op.adu += to_add
            _logger.debug('DAFs-originated demand applied. %s: ADU += %s' %
                (op.name, to_add))