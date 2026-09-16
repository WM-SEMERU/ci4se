def start_logging(self, region, name):
    ct = self.session.client('cloudtrail', region_name=region)
    ct.start_logging(Name=name)
    auditlog(event='cloudtrail.start_logging', actor=self.ns, data={
        'account': self.account.account_name, 'region': region})
    self.log.info('Enabled logging for {} ({})'.format(name, region))