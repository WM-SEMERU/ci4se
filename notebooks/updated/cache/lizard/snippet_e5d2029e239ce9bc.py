def group_selection(request):
    groups = get_user_groups(request.user)
    count = len(groups)
    if count == 1:
        return redirect(groups[0])
    context = {'groups': groups, 'count': count}
    return render(request, 'multitenancy/group-landing.html', context)