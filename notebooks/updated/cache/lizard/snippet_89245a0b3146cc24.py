def update_time_login(u_name):
    entry = TabMember.update(time_login=tools.timestamp()).where(TabMember.
        user_name == u_name)
    entry.execute()