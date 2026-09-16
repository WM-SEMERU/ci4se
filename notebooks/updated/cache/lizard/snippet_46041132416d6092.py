def email(random=random, *args, **kwargs):
    if 'name' in kwargs and kwargs['name']:
        words = kwargs['name']
    else:
        words = random.choice([noun(random=random), name(random=random), 
            name(random=random) + '+spam'])
    return _slugify(words) + '@' + domain(random=random)