def from_custom_template(cls, searchpath, name):
    loader = ChoiceLoader([FileSystemLoader(searchpath), cls.loader])


    class MyStyler(cls):
        env = Environment(loader=loader)
        template = env.get_template(name)
    return MyStyler