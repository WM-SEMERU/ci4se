def random_date():
    d = datetime.datetime.now().date()
    d = d - datetime.timedelta(random.randint(20, 2001))
    return d