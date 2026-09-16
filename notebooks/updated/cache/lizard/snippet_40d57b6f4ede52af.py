def translate_item(self, item_dict):
    if not item_dict.get('title'):
        return None
    if item_dict.get('{wp}post_type', None) == 'attachment':
        return None
    ret_dict = {}
    ret_dict['slug'] = item_dict.get('{wp}post_name') or re.sub(item_dict[
        'title'], ' ', '-')
    ret_dict['ID'] = item_dict['guid']
    ret_dict['title'] = item_dict['title']
    ret_dict['description'] = item_dict['description']
    ret_dict['content'] = item_dict['{content}encoded']
    ret_dict['author'] = {'username': item_dict['{dc}creator'],
        'first_name': '', 'last_name': ''}
    ret_dict['terms'] = item_dict.get('terms')
    ret_dict['date'] = self.convert_date(item_dict['pubDate'], fallback=
        item_dict.get('{wp}post_date', ''))
    return ret_dict