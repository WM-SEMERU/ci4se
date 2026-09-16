def get_comments_data(self, slug):
    all_the_data = []
    for item in self.chan.findall('item'):
        if not item.find('{wp}post_name').text == slug:
            continue
        item_dict = self.item_dict(item)
        if not item_dict or not item_dict.get('title'):
            continue
        slug = item_dict.get('{wp}post_name') or re.sub(item_dict['title'],
            ' ', '-')
        for comment in item.findall('{wp}comment'):
            comment = self.translate_wp_comment(comment)
            comment['slug'] = slug
            all_the_data.append(comment)
    return all_the_data