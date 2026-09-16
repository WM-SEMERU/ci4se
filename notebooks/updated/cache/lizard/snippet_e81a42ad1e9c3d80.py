def global_props(self):
    if self.util.info is None:
        self.util.info = self.steem_instance().get_dynamic_global_properties()
        self.util.total_vesting_fund_steem = Amount(self.util.info[
            'total_vesting_fund_steem']).amount
        self.util.total_vesting_shares = Amount(self.util.info[
            'total_vesting_shares']).amount
        self.util.vote_power_reserve_rate = self.util.info[
            'vote_power_reserve_rate']
    return self.util.info