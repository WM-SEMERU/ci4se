def extract(self, item, list_article_candidate):
    languages_extracted = []
    language_newspaper = None
    for article_candidate in list_article_candidate:
        if article_candidate.language is not None:
            languages_extracted.append(article_candidate.language)
            if article_candidate.extractor == 'newspaper':
                language_newspaper = article_candidate.language
    if not languages_extracted:
        return None
    languages_extracted_set = set(languages_extracted)
    languages_extracted_number = []
    for language in languages_extracted_set:
        languages_extracted_number.append((languages_extracted.count(
            language), language))
    if not languages_extracted_number:
        return None
    if max(languages_extracted_number)[0] == min(languages_extracted_number)[0
        ] and language_newspaper is not None:
        return language_newspaper
    if languages_extracted_number:
        return max(languages_extracted_number)[1]
    else:
        return None