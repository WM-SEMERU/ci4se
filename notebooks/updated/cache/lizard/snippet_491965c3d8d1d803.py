def announcement_view(request, announcement_pk):
    announce = get_object_or_404(Announcement, pk=announcement_pk)
    page_name = 'View Announcement'
    profile = UserProfile.objects.get(user=request.user)
    pin_form = PinForm(request.POST if 'pin' in request.POST else None,
        instance=announce)
    can_edit = announce.incumbent == profile or request.user.is_superuser
    if pin_form.is_valid():
        pin_form.save()
        return HttpResponseRedirect(reverse('managers:view_announcement',
            kwargs={'announcement_pk': announcement_pk}))
    return render_to_response('view_announcement.html', {'page_name':
        page_name, 'pin_form': pin_form, 'can_edit': can_edit,
        'announcement': announce}, context_instance=RequestContext(request))