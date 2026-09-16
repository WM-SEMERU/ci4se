def render_next_step(self, form, **kwargs):
    next_step = self.steps.next
    new_form = self.get_form(next_step, data=self.storage.get_step_data(
        next_step), files=self.storage.get_step_files(next_step))
    self.storage.current_step = next_step
    return self.render(new_form, **kwargs)