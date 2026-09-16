def delete_wiki(self, request, page, rev):
    if self.cleaned_data.get('delete') == 'page' and request.user.has_perm(
        'wakawaka.delete_revision') and request.user.has_perm(
        'wakawaka.delete_wikipage'):
        self._delete_page(page)
        messages.success(request, ugettext('The page %s was deleted' % page
            .slug))
        return HttpResponseRedirect(reverse('wakawaka_index'))
    if self.cleaned_data.get('delete') == 'rev':
        revision_length = len(page.revisions.all())
        if revision_length > 1 and request.user.has_perm(
            'wakawaka.delete_revision'):
            self._delete_revision(rev)
            messages.success(request, ugettext(
                'The revision for %s was deleted' % page.slug))
            return HttpResponseRedirect(reverse('wakawaka_page', kwargs={
                'slug': page.slug}))
        if revision_length <= 1 and not request.user.has_perm(
            'wakawaka.delete_wikipage'):
            messages.error(request, ugettext(
                "You can not delete this revison for %s because it's the only one and you have no permission to delete the whole page."
                 % page.slug))
            return HttpResponseRedirect(reverse('wakawaka_page', kwargs={
                'slug': page.slug}))
        if revision_length <= 1 and request.user.has_perm(
            'wakawaka.delete_revision') and request.user.has_perm(
            'wakawaka.delete_wikipage'):
            self._delete_page(page)
            messages.success(request, ugettext(
                'The page for %s was deleted because you deleted the only revision'
                 % page.slug))
            return HttpResponseRedirect(reverse('wakawaka_index'))