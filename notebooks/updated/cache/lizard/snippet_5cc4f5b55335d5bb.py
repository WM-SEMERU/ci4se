def publishing_prepare_published_copy(self, draft_obj):
    mysuper = super(PublishingModel, self)
    if hasattr(mysuper, 'publishing_prepare_published_copy'):
        mysuper.publishing_prepare_published_copy(draft_obj)