def get_account_info(self):
    attrs = {sconstant.A_BY: sconstant.V_NAME}
    account = SOAPpy.Types.stringType(data=self.auth_token.account_name,
        attrs=attrs)
    params = {sconstant.E_ACCOUNT: account}
    res = self.invoke(zconstant.NS_ZIMBRA_ACC_URL, sconstant.
        GetAccountInfoRequest, params)
    info = AccountInfo()
    info.parse(res)
    return info