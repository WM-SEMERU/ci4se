def ase(dbuser, dbpassword, args, gui):
    if dbuser == 'upload':
        dbpassword = 'cHyuuQH0'
    db = CathubPostgreSQL(user=dbuser, password=dbpassword)
    db._connect()
    server_name = db.server_name
    subprocess.call('ase db {} {}'.format(server_name, args).split())
    if gui:
        args = args.split('-')[0]
        subprocess.call('ase gui {}@{}'.format(server_name, args).split())