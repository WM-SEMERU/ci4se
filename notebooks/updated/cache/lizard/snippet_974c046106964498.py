def fake_KATCP_client_resource_factory(KATCPClientResourceClass,
    fake_options, resource_spec, *args, **kwargs):
    allow_any_request = fake_options.get('allow_any_request', False)


    class FakeKATCPClientResource(KATCPClientResourceClass):

        def inspecting_client_factory(self, host, port, ioloop_set_to):
            real_instance = super(FakeKATCPClientResource, self
                ).inspecting_client_factory(host, port, ioloop_set_to)
            fic, fic_manager = fake_inspecting_client_factory(real_instance
                .__class__, fake_options, host, port, ioloop=ioloop_set_to,
                auto_reconnect=self.auto_reconnect)
            self.fake_inspecting_client_manager = fic_manager
            return fic
    fkcr = FakeKATCPClientResource(resource_spec, *args, **kwargs)
    fkcr_manager = FakeKATCPClientResourceManager(fkcr)
    return fkcr, fkcr_manager