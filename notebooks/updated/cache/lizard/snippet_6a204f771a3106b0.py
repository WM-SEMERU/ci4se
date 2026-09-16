def __query_with_label(cat_id_arr, label=None, num=8, kind='1'):
    return TabPost.select().join(TabPost2Tag, on=TabPost.uid == TabPost2Tag
        .post_id).where((TabPost.kind == kind) & TabPost2Tag.tag_id <<
        cat_id_arr & TabPost.extinfo['def_tag_arr'].contains(label)).order_by(
        TabPost.time_create.desc()).limit(num)