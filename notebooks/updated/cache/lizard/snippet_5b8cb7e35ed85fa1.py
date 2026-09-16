def privacy_options_view(request):
    if 'user' in request.GET:
        user = User.objects.user_with_ion_id(request.GET.get('user'))
    elif 'student_id' in request.GET:
        user = User.objects.user_with_student_id(request.GET.get('student_id'))
    else:
        user = request.user
    if not user:
        messages.error(request, 'Invalid user.')
        user = request.user
    if user.is_eighthoffice:
        user = None
    if user:
        if request.method == 'POST':
            privacy_options_form = save_privacy_options(request, user)
        else:
            privacy_options = get_privacy_options(user)
            privacy_options_form = PrivacyOptionsForm(user, initial=
                privacy_options)
        context = {'privacy_options_form': privacy_options_form,
            'profile_user': user}
    else:
        context = {'profile_user': user}
    return render(request, 'preferences/privacy_options.html', context)