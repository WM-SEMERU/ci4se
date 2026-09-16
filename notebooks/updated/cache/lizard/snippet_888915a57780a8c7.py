def rand_email():
    name = rand_str(random.randint(4, 14), string.ascii_lowercase) + rand_str(
        random.randint(1, 4), string.digits)
    domain = rand_str(random.randint(2, 10), string.ascii_lowercase)
    surfix = random.choice(DOMAIN_SURFIX)
    return '%s@%s.%s' % (name, domain, surfix)