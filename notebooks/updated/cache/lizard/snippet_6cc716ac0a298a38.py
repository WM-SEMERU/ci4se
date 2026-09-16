def get_post(self, rel_url, include_draft=False):
    raw_rel_url = str(rel_url)
    if rel_url.endswith('/index.html'):
        rel_url = rel_url.rsplit('/', 1)[0] + '/'
    post_filename = rel_url[:-1].replace('/', '-')
    post_file_path, post_file_ext = FileStorage.search_instance_file('posts',
        post_filename)
    if (post_file_path is None or post_file_ext is None or 
        get_standard_format_name(post_file_ext) is None):
        return None
    post = Post()
    post.rel_url = raw_rel_url
    post.unique_key = '/post/' + rel_url
    post.format = get_standard_format_name(post_file_ext)
    post.meta, post.raw_content = FileStorage.read_file(post_file_path)
    return post if include_draft or not post.is_draft else None