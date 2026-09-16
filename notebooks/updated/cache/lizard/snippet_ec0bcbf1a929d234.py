def _remove_person_from_group(person, group):
    from karaage.datastores import remove_accounts_from_group
    from karaage.datastores import remove_accounts_from_project
    from karaage.datastores import remove_accounts_from_institute
    a_list = person.account_set
    remove_accounts_from_group(a_list, group)
    for project in group.project_set.all():
        remove_accounts_from_project(a_list, project)
    for institute in group.institute_set.all():
        remove_accounts_from_institute(a_list, institute)