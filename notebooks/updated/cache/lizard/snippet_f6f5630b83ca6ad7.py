def install_database(name, owner, template='template0', encoding='UTF8',
    locale='en_US.UTF-8'):
    create_database(name, owner, template=template, encoding=encoding,
        locale=locale)