def untag(name, tag_name):
    with LOCK:
        by_tag = TAGS.get(tag_name, None)
        if not by_tag:
            return False
        try:
            by_tag.remove(name)
            if not by_tag:
                TAGS.pop(tag_name)
            return True
        except KeyError:
            return False