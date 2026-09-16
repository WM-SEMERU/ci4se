def query_random(num=6, kind='1'):
    return TabWiki.select().where(TabWiki.kind == kind).order_by(peewee.fn.
        Random()).limit(num)