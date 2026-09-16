def convert_to_article(request, entry_id):

    def get_entry_author(entry):
        if not entry.optional_name:
            return 'By Anonymous'
        return 'By %s' % entry.optional_name
    entry = get_object_or_404(YourTipsEntry, pk=entry_id)
    if not entry.converted_article_page:
        tip_section_index_page = (YourTipsSectionIndexPage.objects.
            descendant_of(request.site.root_page).live().first())
        tip_article = YourTipsArticlePage(title='Tip-%s' % str(entry.id),
            slug='yourtips-entry-%s' % cautious_slugify(entry.id), body=
            json.dumps([{'type': 'paragraph', 'value': entry.tip_text}, {
            'type': 'heading', 'value': get_entry_author(entry)}]))
        tip_section_index_page.add_child(instance=tip_article)
        tip_article.save_revision()
        tip_article.unpublish()
        entry.converted_article_page = tip_article
        entry.save()
    return redirect('/admin/pages/%d/edit/' % entry.converted_article_page.id)