def inactive_response(self, request):
    inactive_url = getattr(settings, 'LOGIN_INACTIVE_REDIRECT_URL', '')
    if inactive_url:
        return HttpResponseRedirect(inactive_url)
    else:
        return self.error_to_response(request, {'error': _(
            'This user account is marked as inactive.')})