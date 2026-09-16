def is_selected(self, request):
    current_url = request.get_full_path()
    return self.url == current_url or len([c for c in self.children if c.
        is_selected(request)]) > 0