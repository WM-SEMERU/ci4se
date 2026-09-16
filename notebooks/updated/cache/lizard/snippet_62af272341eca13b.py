def most_seen_creators_by_works_card(work_kind=None, role_name=None, num=10):
    object_list = most_seen_creators_by_works(work_kind=work_kind,
        role_name=role_name, num=num)
    object_list = chartify(object_list, 'num_works', cutoff=1)
    if role_name:
        creators_name = '{}s'.format(role_name.capitalize())
    else:
        creators_name = 'People/groups'
    if work_kind:
        works_name = Work.get_kind_name_plural(work_kind).lower()
    else:
        works_name = 'works'
    card_title = '{} with most {}'.format(creators_name, works_name)
    return {'card_title': card_title, 'score_attr': 'num_works',
        'object_list': object_list}