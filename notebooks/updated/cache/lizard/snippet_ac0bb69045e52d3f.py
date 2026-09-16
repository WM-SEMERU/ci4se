def configure(name, host, port, auth, current):
    Config = ConfigParser.ConfigParser()
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except Exception as e:
            click.echo(e)
            return
    section_name = None
    if current.lower() == 'y':
        section_name = 'Current'
        change_current()
    else:
        section_name = name.capitalize()
    cfgfile = open(filename, 'a')
    Config.add_section(section_name)
    Config.set(section_name, 'host', host)
    Config.set(section_name, 'port', port)
    Config.set(section_name, 'auth', auth)
    Config.set(section_name, 'name', name.capitalize())
    Config.write(cfgfile)
    cfgfile.close()