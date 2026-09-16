def reset(self):
    self.info(self.tr('About to reset..'))
    models = self.data['models']
    models['instances'].store_checkstate()
    models['plugins'].store_checkstate()
    models['instances'].ids = []
    for m in models.values():
        m.reset()
    for b in self.data['buttons'].values():
        b.hide()
    comment_box = self.findChild(QtWidgets.QWidget, 'CommentBox')
    comment_box.hide()
    util.defer(500, self.controller.reset)