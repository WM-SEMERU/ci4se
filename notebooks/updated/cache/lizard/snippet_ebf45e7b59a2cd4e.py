def check_author_info(package_info, *args):
    reason = 'Author name or email missing'
    result = False
    if package_info.get('author') not in BAD_VALUES or package_info.get(
        'author_email') not in BAD_VALUES:
        result = True
    return result, reason, HAS_AUTHOR_INFO