def get_app_relations(app_id, num=20, kind='1'):
    info_tag = MInfor2Catalog.get_first_category(app_id)
    if info_tag:
        return TabPost2Tag.select(TabPost2Tag, TabPost.title.alias(
            'post_title'), TabPost.valid.alias('post_valid')).join(TabPost,
            on=TabPost2Tag.post_id == TabPost.uid).where((TabPost2Tag.
            tag_id == info_tag.tag_id) & (TabPost.kind == kind)).order_by(
            peewee.fn.Random()).limit(num)
    return TabPost2Tag.select(TabPost2Tag, TabPost.title.alias('post_title'
        ), TabPost.valid.alias('post_valid')).join(TabPost, on=TabPost2Tag.
        post_id == TabPost.uid).where(TabPost.kind == kind).order_by(peewee
        .fn.Random()).limit(num)