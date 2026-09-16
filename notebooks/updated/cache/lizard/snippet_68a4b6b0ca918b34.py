def init_widget(self):
    if not self.toast:
        return
    super(AndroidToast, self).init_widget()
    d = self.declaration
    if not self.made_toast:
        self.toast.setDuration(1)
    if d.gravity:
        self.set_gravity(d.gravity)
    if d.show:
        self.set_show(d.show)