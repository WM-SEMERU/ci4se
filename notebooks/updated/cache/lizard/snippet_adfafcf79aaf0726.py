def build_articles_from_article_xmls(article_xmls, detail='full',
    build_parts=None, remove_tags=None):
    poa_articles = []
    for article_xml in article_xmls:
        print('working on ', article_xml)
        article, error_count = build_article_from_xml(article_xml, detail,
            build_parts, remove_tags)
        if error_count == 0:
            poa_articles.append(article)
    return poa_articles