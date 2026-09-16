def list_user_requests_view(request, targetUsername):
    if targetUsername == request.user.username:
        return list_my_requests_view(request)
    targetUser = get_object_or_404(User, username=targetUsername)
    targetProfile = get_object_or_404(UserProfile, user=targetUser)
    page_name = "{0}'s Requests".format(targetUsername)
    requests = Request.objects.filter(owner=targetProfile).exclude(~Q(
        owner__user=request.user), private=True)
    return render_to_response('list_requests.html', {'page_name': page_name,
        'requests': requests, 'targetUsername': targetUsername},
        context_instance=RequestContext(request))