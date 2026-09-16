def operational(ctx, commands, format, xpath):
    mp_pool = multiprocessing.Pool(multiprocessing.cpu_count() * 2)
    for ip in ctx.obj['hosts']:
        mp_pool.apply_async(wrap.open_connection, args=(ip, ctx.obj['conn']
            ['username'], ctx.obj['conn']['password'], wrap.command, [
            commands, format, xpath], ctx.obj['out'], ctx.obj['conn'][
            'connect_timeout'], ctx.obj['conn']['session_timeout'], ctx.obj
            ['conn']['port']), callback=write_out)
    mp_pool.close()
    mp_pool.join()