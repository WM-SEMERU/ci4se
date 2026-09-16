def get_recirc_content(self, published=True, count=3):
    query = self.get_query()
    if not query.get('included_ids'):
        qs = Content.search_objects.search()
        qs = qs.query(TagBoost(slugs=self.tags.values_list('slug', flat=True))
            ).filter(~Ids(values=[self.id])).sort('_score')
        return qs[:count]
    query['included_ids'] = query['included_ids'][:count]
    search = custom_search_model(Content, query, published=published,
        field_map={'feature_type': 'feature_type.slug', 'tag': 'tags.slug',
        'content-type': '_type'})
    return search