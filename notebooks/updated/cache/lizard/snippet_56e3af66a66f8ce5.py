def get_page_args():
    pages = {}
    for arg in request.args:
        re_match = re.findall('page_(.*)', arg)
        if re_match:
            pages[re_match[0]] = int(request.args.get(arg))
    return pages