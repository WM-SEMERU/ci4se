def list_l3_agent_hosting_routers(self, router, **_params):
    return self.get((self.router_path + self.L3_AGENTS) % router, params=
        _params)