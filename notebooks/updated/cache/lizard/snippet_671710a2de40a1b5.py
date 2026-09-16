def indefinite_article(word, gender=MALE, role=SUBJECT):
    return article_indefinite.get((gender[:1].lower(), role[:3].lower()))