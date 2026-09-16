async def connect_controller(self, controller_name=None):
    if not controller_name:
        controller_name = self.jujudata.current_controller()
    if not controller_name:
        raise JujuConnectionError('No current controller')
    controller = self.jujudata.controllers()[controller_name]
    endpoint = controller['api-endpoints'][0]
    accounts = self.jujudata.accounts().get(controller_name, {})
    await self.connect(endpoint=endpoint, uuid=None, username=accounts.get(
        'user'), password=accounts.get('password'), cacert=controller.get(
        'ca-cert'), bakery_client=self.bakery_client_for_controller(
        controller_name))
    self.controller_name = controller_name