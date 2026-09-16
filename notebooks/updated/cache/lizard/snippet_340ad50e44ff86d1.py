def post_comment(form, user):
    if form.is_valid():
        model = form.save(commit=False)
        if user.is_authenticated():
            model.author = user
        model.save()
        return True
    else:
        return False