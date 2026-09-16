def get_account_service(self):
    account_service_url = utils.get_subresource_path_by(self, 'AccountService')
    return account_service.HPEAccountService(self._conn,
        account_service_url, redfish_version=self.redfish_version)