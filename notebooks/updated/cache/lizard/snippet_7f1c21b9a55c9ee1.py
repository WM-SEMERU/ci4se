def cli(env):
    ticket_mgr = SoftLayer.TicketManager(env.client)
    table = formatting.Table(['id', 'subject'])
    for subject in ticket_mgr.list_subjects():
        table.add_row([subject['id'], subject['name']])
    env.fout(table)