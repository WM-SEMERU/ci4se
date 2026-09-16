def get_layer_description_from_canvas(self, layer, purpose):
    if not layer:
        return ''
    try:
        keywords = self.keyword_io.read_keywords(layer)
        if 'layer_purpose' not in keywords:
            keywords = None
    except (HashNotFoundError, OperationalError, NoKeywordsFoundError,
        KeywordNotFoundError, InvalidParameterError, UnsupportedProviderError):
        keywords = None
    self.layer = layer
    if purpose == layer_purpose_hazard['key']:
        self.hazard_layer = layer
    elif purpose == layer_purpose_exposure['key']:
        self.exposure_layer = layer
    else:
        self.aggregation_layer = layer
    if keywords and 'keyword_version' in keywords:
        kw_ver = str(keywords['keyword_version'])
        self.is_selected_layer_keywordless = not is_keyword_version_supported(
            kw_ver)
    else:
        self.is_selected_layer_keywordless = True
    description = layer_description_html(layer, keywords)
    return description