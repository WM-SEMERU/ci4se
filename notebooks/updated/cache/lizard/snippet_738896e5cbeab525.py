def site_content(self, election_day):
    from electionnight.models import PageType
    page_type = PageType.objects.get(model_type=ContentType.objects.get(
        app_label='election', model='electionday'), election_day=election_day)
    site_content = self.get(content_type=ContentType.objects.get_for_model(
        page_type), object_id=page_type.pk, election_day=election_day)
    return {'site': self.serialize_content_blocks(site_content)}