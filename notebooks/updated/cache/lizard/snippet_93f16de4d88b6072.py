def ssh_exec_in_new_loop(server, cmd, timeout=10, **ssh_kwargs):
    task = ssh_exec(server, cmd, timeout=timeout, **ssh_kwargs)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(task)