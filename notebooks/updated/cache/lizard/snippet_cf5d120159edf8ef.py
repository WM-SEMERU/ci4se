def borrow(self, amount, collateral_ratio=None, account=None,
    target_collateral_ratio=None):
    return self.adjust_debt(amount, collateral_ratio, account,
        target_collateral_ratio=target_collateral_ratio)