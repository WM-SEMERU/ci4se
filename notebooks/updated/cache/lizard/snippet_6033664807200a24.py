def update_all_view(self, request):
    LOG.info('Total update requested.')
    total_count = errors = 0
    for repo in self.model.objects.all():
        total_count += 1
        try:
            repo.pull()
        except:
            LOG.exception('While updating %s.' % repo)
            errors += 1
    msg = '{0} repos successfully updated, {1} failed.'.format(total_count,
        errors)
    self.message_user(request, msg, level=messages.SUCCESS)
    return redirect('admin:registry_clonedrepo_changelist')