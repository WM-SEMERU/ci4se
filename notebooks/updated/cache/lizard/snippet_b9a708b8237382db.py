def _list_authors(lst):
    authors = ', '.join([' '.join([a.given_name, a.surname]) for a in lst[0
        :-1]])
    authors += ' and ' + ' '.join([lst[-1].given_name, lst[-1].surname])
    return authors