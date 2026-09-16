def destroy(self):
    super(AndroidTabLayout, self).destroy()
    if self.tabs:
        del self.tabs