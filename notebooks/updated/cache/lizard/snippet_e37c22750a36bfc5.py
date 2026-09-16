def definite_article(word, gender=MALE, role=SUBJECT):
    return article_definite.get((gender[:1].lower(), role[:3].lower()))