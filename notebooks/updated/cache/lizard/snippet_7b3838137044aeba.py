def get_holdings(self, account: SEPAAccount):
    with self._get_dialog() as dialog:
        hkwpd = self._find_highest_supported_command(HKWPD5, HKWPD6)
        responses = self._fetch_with_touchdowns(dialog, lambda touchdown:
            hkwpd(account=hkwpd._fields['account'].type.from_sepa_account(
            account), touchdown_point=touchdown), 'HIWPD')
    holdings = []
    for resp in responses:
        if type(resp.holdings) == bytes:
            holding_str = resp.holdings.decode()
        else:
            holding_str = resp.holdings
        mt535_lines = str.splitlines(holding_str)
        del mt535_lines[0]
        mt535 = MT535_Miniparser()
        holdings.extend(mt535.parse(mt535_lines))
    if not holdings:
        logger.debug(
            'No HIWPD response segment found - maybe account has no holdings?')
    return holdings