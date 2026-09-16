def contact(request, slug, template_name='staffmembers/contact.html',
    success_url='/staff/contact/done/', email_subject_template=
    'staffmembers/emails/subject.txt', email_body_template=
    'staffmembers/emails/body.txt'):
    member = get_object_or_404(StaffMember, slug__iexact=slug, is_active=True)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = render_to_string(email_subject_template, {'member':
                member})
            subject = ''.join(subject.splitlines())
            message = render_to_string(email_body_template, {'name': form.
                cleaned_data['name'], 'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message']})
            EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [
                member.email], headers={'Reply-To': form.cleaned_data['email']}
                ).send()
            return HttpResponseRedirect(success_url)
    else:
        initial = {}
        if not request.user.is_anonymous():
            initial = {'name': '%s %s' % (request.user.first_name, request.
                user.last_name), 'email': request.user.email}
        form = ContactForm(initial=initial)
    return render_to_response(template_name, {'form': form, 'member':
        member}, context_instance=RequestContext(request))