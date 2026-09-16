def clean_all_trash_pages_from_all_spaces(confluence):
    limit = 50
    flag = True
    i = 0
    while flag:
        space_lists = confluence.get_all_spaces(start=i * limit, limit=limit)
        if space_lists and len(space_lists) != 0:
            i += 1
            for space_list in space_lists:
                print('Start review the space with key = ' + space_list['key'])
                clean_pages_from_space(confluence=confluence, space_key=
                    space_list['key'])
        else:
            flag = False
    return 0