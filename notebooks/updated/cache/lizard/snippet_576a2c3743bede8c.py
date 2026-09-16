def delete_announcement_view(request, id):
    if request.method == 'POST':
        post_id = None
        try:
            post_id = request.POST['id']
        except AttributeError:
            post_id = None
        try:
            a = Announcement.objects.get(id=post_id)
            if request.POST.get('full_delete', False):
                a.delete()
                messages.success(request, 'Successfully deleted announcement.')
            else:
                a.expiration_date = datetime.datetime.now()
                a.save()
                messages.success(request, 'Successfully expired announcement.')
        except Announcement.DoesNotExist:
            pass
        return redirect('index')
    else:
        announcement = get_object_or_404(Announcement, id=id)
        return render(request, 'announcements/delete.html', {'announcement':
            announcement})