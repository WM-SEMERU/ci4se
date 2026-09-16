def form_invalid(self, form):
    context = self.get_context_data(form=form)
    return render_modal_workflow(self.request, '{0}/chooser.html'.format(
        self.template_dir), '{0}/chooser.js'.format(self.template_dir), context
        )