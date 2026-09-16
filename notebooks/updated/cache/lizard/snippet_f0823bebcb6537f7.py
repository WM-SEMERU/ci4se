async def _get_smallest_env(self):

    async def slave_task(mgr_addr):
        r_manager = await self.env.connect(mgr_addr, timeout=TIMEOUT)
        ret = await r_manager.get_agents(addr=True)
        return mgr_addr, len(ret)
    sizes = await create_tasks(slave_task, self.addrs, flatten=False)
    return sorted(sizes, key=lambda x: x[1])[0][0]