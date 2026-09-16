def evaluation(self, evl):
    if isinstance(evl, str):
        evl = self.tags_evaluation.find(evl)
    if isinstance(evl, Tag):
        evl = SelectedTag(tag_id=evl.ident, tags=self.tags_evaluation)
    javabridge.call(self.jobject, 'setEvaluation',
        '(Lweka/core/SelectedTag;)V', evl.jobject)