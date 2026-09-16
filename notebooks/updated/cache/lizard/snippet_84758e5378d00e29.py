def form_valid(self, form):
    response = super().form_valid(form)
    messages.success(self.request, self.success_message)
    return response