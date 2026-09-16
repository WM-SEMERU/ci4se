def _login_snmp(self):
    logger.info('Trying to grab stats by SNMP...')
    from glances.stats_client_snmp import GlancesStatsClientSNMP
    self.stats = GlancesStatsClientSNMP(config=self.config, args=self.args)
    if not self.stats.check_snmp():
        self.log_and_exit('Connection to SNMP server failed')
        return False
    return True