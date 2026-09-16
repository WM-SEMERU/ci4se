def checkout(config, rev):
    with open(config, 'r'):
        main.checkout(yaml.load(open(config)), rev)