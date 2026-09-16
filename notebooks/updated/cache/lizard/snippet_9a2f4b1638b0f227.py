def post(self, id):
    model = self.model.objects.only('id').get_or_404(id=id)
    follow, created = Follow.objects.get_or_create(follower=current_user.id,
        following=model, until=None)
    count = Follow.objects.followers(model).count()
    if not current_app.config['TESTING']:
        tracking.send_signal(on_new_follow, request, current_user)
    return {'followers': count}, 201 if created else 200